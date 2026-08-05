# Well-Architected Review — Acme Customer Support Assistant (`support-rag`)

**Scope reviewed:** `infra/main.tf`, `src/handler.py`, `README.md`
**Workload:** Public-facing RAG chat assistant, `us-east-1`, ~40k conversations/month, +15% MoM
**Reviewed against:** AWS Well-Architected Framework (six pillars) + Generative AI Lens
**Verdict:** **Not ready for a platform review as-is.** There is one active, unresolved data-isolation defect that exposes customer PII across tenant boundaries. Expect that to dominate the entire meeting.

---

## 1. Executive summary

This workload works, and that is roughly the extent of the good news. It was built as a prototype — single file, single region, hardcoded secret, wildcard IAM — and then put in front of external customers on the public internet without the hardening step in between. The four "known issues" in the README are not four independent problems; they are four visible symptoms of the same set of root causes, and every one of them is diagnosable from the code.

The single most serious finding is that **the retrieval layer has no tenant isolation whatsoever**. `customer_id` is documented in the handler's docstring but is never read, never passed to `retrieve()`, and never used as a metadata filter. Every customer's billing history and ticket records sit in one S3 bucket, feeding one knowledge base, backed by one vector index, queried with no filter. The README's "one incident where the assistant surfaced another customer's ticket summary" was not an anomaly — it is the designed behaviour of this system, and it will recur. Treat that incident as a probable reportable privacy breach and get legal/privacy involved independently of the engineering fix.

Beyond that, the review panel will find: an authentication scheme that cannot work (a shared static API key in a browser-embedded widget), IAM roles with `bedrock:*` and `s3:*` on `Resource = "*"`, no encryption configuration on a bucket holding PII, no guardrails, no evaluation harness, no observability, no cost attribution, and a Terraform module that is missing enough resources that the deployed production stack cannot possibly match what is in this repo.

**Findings by severity:** 6 Critical · 11 High · 14 Medium · 8 Low

**Pillar readiness at a glance:**

| Pillar | Rating | One-line assessment |
|---|---|---|
| Security | **Critical risk** | No tenant isolation, no real authN, wildcard IAM, unencrypted PII store |
| Reliability | **High risk** | No retry/throttle handling, timeout mismatch, single region, no state locking |
| Performance Efficiency | **Medium risk** | Over-retrieval, no reranking, no caching, no streaming, untuned runtime |
| Cost Optimization | **High risk** | Zero cost attribution — the "unexplainable bill" is a direct consequence |
| Operational Excellence | **High risk** | No observability, no eval harness, no CI/CD, significant IaC drift |
| Sustainability | **Low-Medium risk** | Wasted compute from over-retrieval, oversized generations, x86 runtime |
| Responsible AI (GenAI Lens) | **Critical risk** | Prompt actively instructs the model to hallucinate; temperature 0.9; no guardrails |

---

## 2. The five things you will get hammered on

Ordered by how much airtime they will consume, not strictly by CVSS.

### 2.1 There is no tenant isolation in retrieval — CRITICAL

`src/handler.py:39-46` accepts `customer_id` in the request body and then discards it. `retrieve()` (`src/handler.py:28-36`) issues a pure semantic search across the entire index with `numberOfResults: 20` and no `filter` clause.

Compounding it, per the README architecture notes, the billing team's ETL writes account records — billing history, open tickets, plan tier — into **the same S3 bucket** as the public help-centre articles. Public marketing content and confidential per-customer PII share one bucket, one knowledge base, one vector index, and one retrieval path.

The consequence: a question like "why was my invoice higher last month" performs a similarity search that will happily return the closest-matching *other customer's* billing dispute, and that text is then interpolated straight into the system prompt at `src/handler.py:55`. The model has no way to know the record is not the caller's — in fact the prompt at `src/handler.py:20` explicitly tells it "You have access to the customer's full account history, billing records and open tickets," which primes it to present whatever it is given as the caller's own data.

You cannot fix this with prompt engineering. It requires an enforced filter at the retrieval layer.

**Required fix (all three, not one of them):**
1. Attach `customer_id` metadata to every account record at ingestion and pass a retrieval filter: `retrievalConfiguration.vectorSearchConfiguration.filter = {"equals": {"key": "customer_id", "value": <authenticated_customer_id>}}`.
2. Take `customer_id` from a verified identity claim (JWT sub), **never** from the request body — a body-supplied ID is just an IDOR vulnerability with extra steps.
3. Split the data into two knowledge bases: one for public help-centre content (no filter needed) and one for per-customer records (filter mandatory). Two retrieval calls, merged. This makes "unfiltered access to public docs" the default-safe path and "filtered access to PII" a separate, auditable code path.

Additionally, add a Bedrock Guardrail with PII detection on the **output** as a backstop, so a filter regression does not immediately become a second breach.

### 2.2 The authentication model cannot work by construction — CRITICAL

`src/handler.py:16` hardcodes `API_KEY = "sk-acme-support-2f8a91"` — checked into git, baked into the deployment zip, shared across all callers, never rotated. `infra/main.tf:75` acknowledges this in a comment: `# auth handled in the Lambda via a shared API key header`.

The fatal detail is in the README: the widget is **embedded on the public support site**. For the browser widget to send `x-api-key`, that key must be shipped to the browser. It is therefore public. Anyone can open devtools, read it, and call `POST /chat` directly, with no rate limit (§4.2.4), no WAF, and no per-caller quota — against a Bedrock account billed per token.

Also note `src/handler.py:40` uses `!=` for the comparison, which is timing-unsafe; that is the least of the problems here but a reviewer will mention it.

**Required fix:** Real end-user authentication. Cognito (or your existing customer IdP) issuing a JWT, validated by an **API Gateway JWT authorizer** at `aws_apigatewayv2_route.chat` — not in Lambda code. The `sub`/`custom:customer_id` claim from that token becomes the authoritative tenant identifier for §2.1. Rotate `sk-acme-support-2f8a91` and treat it as compromised — it has been in git history and in a public-facing bundle.

### 2.3 The prompt is explicitly configured to produce confident hallucinations — CRITICAL

The README says answers are "confidently wrong maybe 1 in 20 times." That number is not mysterious. Two lines cause it:

- `src/handler.py:21` — `"If the context does not contain the answer, use your general knowledge to help anyway."` This is a direct instruction to fabricate. On a **billing and product support** assistant, "general knowledge" means the model inventing Acme's refund windows, cancellation terms, and pricing tiers. That is a contractual and regulatory exposure, not just a quality issue.
- `src/handler.py:54` — `"temperature": 0.9`. For a factual, grounded retrieval assistant this should be at or near `0`. At 0.9 the model samples creatively over its own uncertainty, which is precisely the mechanism that turns "unsure" into "fluently wrong."

Two more contributors: `retrieve()` (`src/handler.py:36`) returns an empty string when the KB matches nothing, and the empty context then hits the "use your general knowledge" instruction — worst case, maximum-confidence, zero-grounding. And the retrieval results carry source locations which the code throws away, so answers ship with **no citations** and support leads have no way to spot-check them.

**Required fix:** Set `temperature: 0`. Replace the fallback instruction with an explicit refusal path ("If the context does not contain the answer, say you don't have that information and offer to connect the customer to a support agent"). Short-circuit to that refusal in code when `retrievalResults` is empty. Return source citations alongside the answer. Add a Bedrock Guardrail with contextual grounding checks enabled to filter ungrounded responses at the platform layer.

### 2.4 Nobody can explain the bill because nothing is instrumented to explain it — HIGH

"Bedrock spend has roughly tripled since launch and nobody can explain the shape of the bill." There is not one mechanism in this stack that could explain it:

- **Zero cost allocation tags.** Not a single resource in `infra/main.tf` has a `tags` block. Cost Explorer cannot break spend down by feature, team, or environment. This alone makes the question unanswerable.
- **Bedrock model invocation logging is not enabled**, so there is no per-request record of input/output token counts.
- **No structured logging** in the handler — no request ID, no token usage, no latency, no model ID emitted. `resp` at `src/handler.py:59` contains usage metadata that is parsed for `content[0].text` and otherwise discarded.
- **No AWS Budgets and no Cost Anomaly Detection**, so the tripling was noticed on an invoice rather than on day one.

The likely *drivers* of the tripling, all visible in the code:

| Driver | Evidence | Effect |
|---|---|---|
| Over-retrieval | `numberOfResults: 20` (`handler.py:33`) | 20 chunks of input tokens on **every** call, no reranking, no top-k trim |
| Oversized generations | `max_tokens: 4096` + `temperature: 0.9` + "Be thorough" (`handler.py:19,53,54`) | Long, rambling outputs — output tokens are the expensive ones |
| Abandoned-but-still-billed calls | Lambda timeout 300s vs API GW 30s (§2.5) | You pay for full Bedrock generations the client already gave up on |
| Unauthenticated public endpoint | §2.2 | Anyone can burn your token budget |
| Silent retry amplification | No explicit retry config; boto3 defaults retry throttles | 429s (which you have) generate additional billable attempts |
| No caching | No cache layer anywhere | Support traffic is extremely head-heavy; the same 50 FAQs are regenerated from scratch thousands of times |
| OpenSearch Serverless floor | `aws_opensearchserverless_collection` (`main.tf:17`) | AOSS bills a minimum OCU floor 24/7 regardless of traffic — frequently the surprise line item at this scale, and it is *not* Bedrock spend, which may be part of why the shape is confusing |

**Required fix, in order:** tag every resource; enable Bedrock model invocation logging to CloudWatch/S3; emit token counts per request as CloudWatch EMF metrics; set a Budget with an anomaly detector. Then reduce: retrieve 20 → rerank → pass top 3-5; drop `max_tokens` to something calibrated to real answer length (likely 1024); add prompt caching for the static system-prompt prefix; add an exact-match/semantic cache. Separately, price AOSS against alternatives — at 40k conversations/month the AOSS capacity floor may cost more than the inference.

### 2.5 The Lambda timeout is 10× the API Gateway timeout — HIGH

`infra/main.tf:55` sets `timeout = 300`. API Gateway HTTP APIs cap integration timeout at 30 seconds. So for any request slower than 30s, the client receives a 504 while the Lambda keeps running for up to another 4.5 minutes — completing a Bedrock generation, paying for every token, and writing the result nowhere.

This is the mechanical link between two README issues: "latency spikes to 20s+" and "spend has tripled." Every timed-out request is billed at full cost for zero delivered value, and at 20s baseline latency you are already at the edge of the cliff.

**Required fix:** Set Lambda `timeout` to ~29s so failures are fast and cheap. Then attack the latency itself — the fix for a 20s wait is not a longer timeout, it is **response streaming**. Switch to `invoke_model_with_response_stream` and deliver tokens via Lambda response streaming or a WebSocket API. Time-to-first-token drops to ~1s and the 20s total becomes invisible to the user. Combined with cutting 20 chunks down to 5, the actual generation time will drop substantially too.

---

## 3. Root-cause map: your known issues → actual causes

| README symptom | Root cause(s) | Finding |
|---|---|---|
| Latency spikes to 20s+ | 20 retrieved chunks inflating input; `max_tokens: 4096`; no streaming; no caching; no reranking | PERF-1, PERF-3, PERF-4, §2.5 |
| Occasional 429s from Bedrock | No retry config with adaptive/jittered backoff; no cross-region inference profile; no provisioned throughput; single region (us-east-1 is the most contended) | REL-1, REL-2 |
| Bedrock spend tripled, bill shape unexplainable | No tags, no invocation logging, no token metrics, no budget; plus over-retrieval, oversized generations, abandoned-call billing, unauthenticated endpoint | §2.4 |
| "Confidently wrong" ~1 in 20, unmeasurable | `temperature: 0.9`; prompt instructs fallback to general knowledge; no grounding guardrail; no citations; empty-context path unguarded. **Unmeasurable** because there is no eval harness and no feedback capture | §2.3, OPS-2 |
| Surfaced another customer's ticket summary | No `customer_id` filter on retrieval; PII and public docs co-located in one bucket/KB/index; identity taken from request body | §2.1 |

Every listed symptom is fully explained by code visible in this repo. There is nothing here that requires further investigation to diagnose — which is itself the argument for prioritising the fixes over more analysis.

---

## 4. Full findings by pillar

Severity: **C**ritical / **H**igh / **M**edium / **L**ow

### 4.1 Security

| ID | Sev | Finding | Location |
|---|---|---|---|
| SEC-1 | C | No tenant isolation on retrieval; `customer_id` accepted and ignored | `handler.py:28-46` |
| SEC-2 | C | Tenant identity would be taken from request body (IDOR) rather than a verified claim | `handler.py:3,43` |
| SEC-3 | C | Hardcoded shared API key in source, in git, shipped to a public browser widget | `handler.py:16,40` |
| SEC-4 | C | PII and public content co-mingled in one S3 bucket / KB / vector index — no data classification boundary | `main.tf:13`, README |
| SEC-5 | H | IAM: `bedrock:*` on `Resource = "*"` — permits `DeleteKnowledgeBase`, model customization, provisioned throughput purchases, not just inference | `main.tf:110-113` |
| SEC-6 | H | IAM: `s3:GetObject/ListBucket/PutObject` on `Resource = "*"` — read **and write** to every bucket in the account | `main.tf:115-118` |
| SEC-7 | H | KB role granted the `AmazonBedrockFullAccess` managed policy | `main.tf:140-143` |
| SEC-8 | H | S3 bucket holding customer PII has no SSE-KMS, no public access block, no versioning, no TLS-only bucket policy, no access logging | `main.tf:13-15` |
| SEC-9 | H | No Bedrock Guardrail — no PII filtering, no denied topics, no jailbreak detection, no grounding check | absent |
| SEC-10 | H | No WAF and no throttling on a public, effectively unauthenticated endpoint | `main.tf:66-88` |
| SEC-11 | M | OpenSearch Serverless collection declared with no encryption, network, or data access policy — the vector store's exposure and key management are undefined in code | `main.tf:17-20` |
| SEC-12 | M | Retrieved content interpolated directly into the system prompt with no delimiting or provenance marking — indirect prompt injection via help-centre articles or ETL'd records | `handler.py:55` |
| SEC-13 | M | No input validation: `question` length is unbounded (token-cost DoS and injection surface); `isBase64Encoded` bodies unhandled | `handler.py:43-44` |
| SEC-14 | M | Lambda not in a VPC; no VPC endpoints for Bedrock/S3 — all traffic traverses public AWS endpoints | `main.tf:49-64` |
| SEC-15 | M | No audit trail of prompts, retrievals, or responses; Bedrock invocation logging disabled — the tenant-leak incident is **not forensically investigable** | absent |
| SEC-16 | L | Timing-unsafe API key comparison (`!=` rather than `hmac.compare_digest`) | `handler.py:40` |
| SEC-17 | L | No API Gateway access logging on the prod stage | `main.tf:84-88` |
| SEC-18 | L | No KMS CMK anywhere; all encryption relies on AWS-managed keys | throughout |

**Note on SEC-1/SEC-4:** the cross-customer disclosure that already occurred should be routed to privacy/legal for breach-notification assessment (GDPR Art. 33 timelines are short, and CCPA/state equivalents may apply depending on customer geography). That is a parallel track to the engineering fix, and the platform review will ask whether it happened.

### 4.2 Reliability

| ID | Sev | Finding | Location |
|---|---|---|---|
| REL-1 | H | No explicit boto3 retry configuration — no adaptive mode, no jittered backoff, no fallback model, despite documented 429s | `handler.py:11-12` |
| REL-2 | H | Single region, on-demand throughput only; no cross-region inference profile, no provisioned throughput, no capacity plan against a workload growing 15% MoM | `main.tf:7-9,61` |
| REL-3 | H | Lambda timeout (300s) exceeds API Gateway's 30s cap by 10× — see §2.5 | `main.tf:55` |
| REL-4 | H | No remote Terraform backend and no state locking; state is local and contains sensitive values. Concurrent `terraform apply` from two laptops corrupts prod state | `main.tf:1-5` |
| REL-5 | M | No reserved or provisioned concurrency; a traffic spike can exhaust account-wide Lambda concurrency and take down unrelated functions | `main.tf:49-64` |
| REL-6 | M | Unhandled exceptions throughout: `json.loads(event["body"])`, `body["question"]`, `resp["retrievalResults"]`, `["content"][0]["text"]` all raise on malformed input or empty results, surfacing as opaque 502s | `handler.py:43-61` |
| REL-7 | M | Empty retrieval result produces an empty context that is then fed to the "use general knowledge" instruction rather than short-circuiting to a refusal | `handler.py:36,46` |
| REL-8 | M | Nightly KB re-sync has no success/failure monitoring — a silently failing ingestion means silently stale answers, undetectable from the outside | README, absent from TF |
| REL-9 | M | No backup or recovery story: S3 unversioned, no replication, no AOSS snapshot policy, no documented RTO/RPO, no DR runbook | `main.tf:13-20` |
| REL-10 | L | No health check endpoint, no synthetic canary | absent |
| REL-11 | L | No idempotency handling on retries | `handler.py:39` |

### 4.3 Performance Efficiency

| ID | Sev | Finding | Location |
|---|---|---|---|
| PERF-1 | H | `numberOfResults: 20` with no reranking — inflates input tokens and TTFT, and degrades answer quality through "lost in the middle" context dilution. Retrieve wide, rerank, pass 3-5 | `handler.py:33` |
| PERF-2 | H | No response streaming; users wait for the complete generation before seeing anything | `handler.py:48` |
| PERF-3 | M | No caching layer. Support traffic is head-heavy — the same FAQs are re-embedded and re-generated indefinitely. An exact-match cache keyed on normalized question hash would deflect a large fraction at near-zero cost | absent |
| PERF-4 | M | No Bedrock prompt caching for the static system-prompt prefix | `handler.py:48-59` |
| PERF-5 | M | `max_tokens: 4096` combined with "Be thorough and helpful" produces longer answers than a support widget can display, at direct latency and cost | `handler.py:19,53` |
| PERF-6 | M | Single model (Claude 3.5 Sonnet) for all traffic; no tiering — simple/FAQ queries could route to Haiku at a fraction of cost and latency | `main.tf:61` |
| PERF-7 | L | Lambda memory (1024MB) never tuned; no Lambda Power Tuning run | `main.tf:56` |
| PERF-8 | L | x86 runtime; no `architectures = ["arm64"]` (~20% price-performance gain, no code change for this workload) | `main.tf:53` |
| PERF-9 | L | Chunking strategy and embedding dimensionality never specified — running on defaults, never evaluated against your actual document shapes | `main.tf:22-45` |

### 4.4 Cost Optimization

| ID | Sev | Finding | Location |
|---|---|---|---|
| COST-1 | H | **Zero cost allocation tags on any resource** — makes the "unexplainable bill" structurally unanswerable | `main.tf` throughout |
| COST-2 | H | No Bedrock invocation logging and no token-usage metrics — no per-request or per-feature cost attribution | absent |
| COST-3 | H | Timed-out-but-still-running Lambdas pay full Bedrock cost for undelivered responses | `main.tf:55` |
| COST-4 | H | Unauthenticated public endpoint with no rate limit is an open token-spend vector | §2.2 |
| COST-5 | M | No AWS Budgets, no Cost Anomaly Detection — a 3× increase went unnoticed until invoicing | absent |
| COST-6 | M | OpenSearch Serverless minimum OCU floor bills 24/7 independent of traffic; at 40k conv/month this may exceed inference spend. Evaluate Aurora pgvector or S3 Vectors | `main.tf:17-20` |
| COST-7 | M | No CloudWatch log retention policy — log groups are created implicitly and retain forever | absent |
| COST-8 | M | Over-retrieval + oversized `max_tokens` + no caching are the three largest controllable inference cost levers, all currently set to the expensive option | `handler.py:33,53` |
| COST-9 | L | No per-customer token quota or abuse ceiling | absent |

### 4.5 Operational Excellence

| ID | Sev | Finding | Location |
|---|---|---|---|
| OPS-1 | H | No observability: no structured logging, no correlation IDs, no X-Ray/ADOT tracing, no custom metrics, no alarms, no dashboards. The system is a black box in production | `handler.py` throughout |
| OPS-2 | H | **No evaluation harness.** "Confidently wrong 1 in 20 but we can't measure it" is a tooling gap, not a mystery. Needs a golden question set with expected answers, offline scoring on faithfulness/groundedness/context-precision run in CI on every prompt or model change, plus online signals (thumbs up/down, human-escalation rate, deflection rate) | absent |
| OPS-3 | H | Significant IaC drift — the deployed stack cannot match this repo (see §5). Nobody can reason accurately about production from this code | `main.tf` |
| OPS-4 | M | No CI/CD, no tests, no staging environment. `cd infra && terraform apply` from a laptop straight to a production system serving external customers | README:30-34 |
| OPS-5 | M | Prompt is a string literal in the handler — no versioning, no A/B capability, no rollback independent of a code deploy. Use Bedrock Prompt Management or at minimum externalize and version it | `handler.py:18-25` |
| OPS-6 | M | No feedback capture from support leads into a labeled dataset — the one signal you have about quality is anecdotal and evaporates | absent |
| OPS-7 | M | No runbooks, no alarms, no defined on-call, and no documented remediation for the tenant-leak incident | README:21-28 |
| OPS-8 | M | Region, resource names, and model ID hardcoded; no variables, no environment separation, no modules | `main.tf` throughout |
| OPS-9 | L | No model deprecation/upgrade process; model ID pinned inline in Terraform with no migration or regression-test plan | `main.tf:61` |
| OPS-10 | L | Docstring at `handler.py:3` documents a `customer_id` parameter the code does not implement — documentation actively misleads readers about the security model | `handler.py:3` |

### 4.6 Sustainability

| ID | Sev | Finding |
|---|---|---|
| SUS-1 | M | Retrieving 4× more context than needed and generating up to 4096 tokens per answer wastes compute on every single request at 40k conversations/month |
| SUS-2 | L | No caching means identical work is repeated indefinitely |
| SUS-3 | L | x86 rather than Graviton; untuned Lambda memory |
| SUS-4 | L | Lambdas running up to 270s past client abandonment burn compute for discarded output |

### 4.7 Responsible AI (Generative AI Lens)

| ID | Sev | Finding | Location |
|---|---|---|---|
| RAI-1 | C | System prompt explicitly instructs the model to answer from general knowledge when context is missing — on a billing/product assistant this authorizes fabrication of contractual terms | `handler.py:21` |
| RAI-2 | C | `temperature: 0.9` on a factual grounded-retrieval task | `handler.py:54` |
| RAI-3 | H | No guardrails of any kind: no PII redaction, no denied topics, no jailbreak filtering, no contextual grounding check, no toxicity filtering on input or output | absent |
| RAI-4 | H | No citations returned — retrieval results carry source locations that are discarded at `handler.py:36`, leaving customers and support leads unable to verify any claim | `handler.py:36` |
| RAI-5 | M | No "I don't know" path and no human-escalation handoff. A support assistant with no route to a human is a customer-experience and compliance gap | `handler.py:39-62` |
| RAI-6 | M | Prompt claims "You have access to the customer's full account history" — priming the model to assert ownership of whatever text it is handed, which converted the retrieval bug in §2.1 into a confident misrepresentation | `handler.py:20` |
| RAI-7 | M | It is described as a chat assistant but is entirely stateless single-turn — no conversation history is passed. Follow-up questions ("what about the other one?") cannot work | `handler.py:56` |
| RAI-8 | L | No verification that the widget discloses to customers that they are interacting with an AI system | README:10-11 |

---

## 5. IaC completeness — the deployed stack does not match this repo

Independent of design quality, `infra/main.tf` is missing resources that a working production deployment must have. Either they were created manually (drift — nobody can trust this code as a description of production) or this Terraform has never successfully produced the running system. A reviewer will spot this quickly and it will undermine confidence in everything else you present.

Missing:

1. **`aws_lambda_permission`** granting `apigateway.amazonaws.com` permission to invoke `acme-support-chat`. Without the resource-based policy the integration returns 500 on every request. It is live, so this was added out of band.
2. **`aws_bedrockagent_data_source`** — the knowledge base is declared with no data source. The entire S3→KB ingestion pipeline, including the nightly re-sync described in the README, is unmanaged.
3. **OpenSearch Serverless policies** — `aws_opensearchserverless_security_policy` (encryption **and** network) and `aws_opensearchserverless_access_policy`. AOSS collections cannot be created without an encryption policy, so these exist outside Terraform. This means the collection's network exposure and key management are invisible in code (SEC-11).
4. **The vector index itself** (`support-idx`) is referenced at `main.tf:40` but never created — index creation with the correct mappings is a manual prerequisite.
5. **`aws_cloudwatch_log_group`** for `/aws/lambda/acme-support-chat` — created implicitly with infinite retention (COST-7).
6. **The cron Lambda** that performs the nightly KB re-sync (README:17) does not appear in Terraform at all.
7. **`terraform { backend }`** block — no remote state, no locking (REL-4).
8. **`tags`** on every resource (COST-1).
9. **`aws_apigatewayv2_stage` throttling settings and `access_log_settings`** (SEC-10, SEC-17).

---

## 6. Remediation plan

### Immediate — before the platform review (days)

These are the items where "we've already fixed it" changes the tone of the meeting entirely.

1. **Stop the tenant leak.** Ship the retrieval filter (§2.1). If a full fix needs the ETL to re-emit records with `customer_id` metadata, the interim mitigation is to remove per-customer records from the knowledge base entirely and serve help-centre content only — degraded but safe. Do not leave it as-is through the review.
2. **Set `temperature: 0`** and replace the "use your general knowledge" instruction with an explicit refusal path (§2.3). One-line change, measurable quality impact, and the single cheapest credibility win available.
3. **Set Lambda `timeout = 29`** (§2.5). Stops paying for abandoned generations immediately.
4. **Rotate the API key** and get it out of source into Secrets Manager as a stopgap while real authN is built (§2.2).
5. **Tag every resource** and turn on Bedrock invocation logging, a Budget, and Cost Anomaly Detection (§2.4). Without these you will walk into the review still unable to answer the cost question.
6. **Scope the two IAM policies** from `Resource = "*"` down to the specific model ARN and the specific bucket ARN; replace `AmazonBedrockFullAccess` on the KB role with a scoped inline policy (SEC-5/6/7).
7. **Reduce `numberOfResults` to 5** and `max_tokens` to 1024 as an immediate cost and latency measure, pending proper reranking (PERF-1, PERF-5).

### Short term (30 days)

8. Cognito/IdP JWT authorizer at API Gateway; derive `customer_id` from the verified claim (SEC-2, SEC-3).
9. Split into two knowledge bases — public content and per-customer records — with the filter mandatory on the latter (SEC-4).
10. Bedrock Guardrails: PII filtering on output, contextual grounding checks, denied topics, jailbreak detection (SEC-9, RAI-3).
11. S3 hardening: SSE-KMS with a CMK, public access block, versioning, TLS-only bucket policy, access logging (SEC-8).
12. Bring the missing resources in §5 into Terraform; migrate state to S3 with DynamoDB locking (OPS-3, REL-4).
13. Observability baseline: Powertools for AWS Lambda for structured logging and tracing, EMF metrics for token counts, latency percentiles, retrieval hit rates, and error rates; alarms on p99 latency, 4xx/5xx rate, and daily token spend (OPS-1).
14. Explicit boto3 retry configuration with adaptive mode; evaluate a cross-region inference profile for the 429s (REL-1, REL-2).
15. Return citations with every answer (RAI-4).
16. WAF with rate-based rules in front of the API; stage-level throttling (SEC-10).
17. Harden the handler: input validation, question length cap, structured error responses, empty-retrieval short-circuit (SEC-13, REL-6, REL-7).

### Medium term (90 days)

18. **Evaluation harness** — golden dataset, offline groundedness/relevance scoring in CI on every prompt and model change, plus online feedback capture. This is what converts "confidently wrong 1 in 20" from folklore into a tracked metric with a target (OPS-2, OPS-6).
19. Response streaming end to end (PERF-2).
20. Reranking stage; semantic caching; prompt caching; model tiering with Haiku for simple queries (PERF-1, PERF-3, PERF-4, PERF-6).
21. CI/CD with a staging environment; no more `terraform apply` from a laptop (OPS-4).
22. Prompt externalization and versioning via Bedrock Prompt Management (OPS-5).
23. Conversational memory so it is actually a chat assistant (RAI-7).
24. Human escalation path from the widget (RAI-5).
25. Multi-region / DR posture and documented RTO/RPO commensurate with a customer-facing system (REL-9).
26. Cost model review for OpenSearch Serverless vs. alternatives at your actual scale (COST-6).

---

## 7. Questions the panel will ask that you need answers to

Have these ready. Not having an answer is worse than having a bad one.

1. Was the cross-customer ticket disclosure assessed for breach notification, and by whom? How many customers were affected? How would you know?
2. How would you detect it if it happened again today? *(Current answer: you would not — SEC-15.)*
3. What is your RTO/RPO for a customer-facing system, and what happens if `us-east-1` Bedrock degrades?
4. What is the cost per conversation, and what was it at launch? *(Current answer: unknown — COST-1/2.)*
5. What is your target accuracy, how is it measured, and what is the trend? *(Current answer: no measurement exists — OPS-2.)*
6. Who can invoke this API today, and how do you know? *(Current answer: anyone who opened devtools — SEC-3.)*
7. What is the blast radius if the Lambda role is compromised? *(Current answer: read/write to every S3 bucket in the account plus full Bedrock control-plane access — SEC-5/6.)*
8. What is in the knowledge base, what is its data classification, and who approved co-locating public and confidential content?
9. How do you roll back a bad prompt change without a code deploy?
10. What is your capacity plan at 15% MoM growth against on-demand Bedrock quotas?

---

## 8. What is genuinely good

Worth saying out loud, both because it is true and because it tells the panel the foundations are sound enough to fix rather than rebuild:

- The architecture is the right shape. API Gateway → Lambda → Bedrock Knowledge Base over a managed vector store is the correct, boring, well-supported pattern for this workload. None of the findings above require re-architecting.
- Serverless throughout means no patching burden and genuine scale-to-zero.
- Infrastructure is in Terraform rather than click-ops, even if incomplete — there is something to fix.
- The model ID is version-pinned (`anthropic.claude-3-5-sonnet-20241022-v2:0`) rather than floating, which avoids silent behavioural drift.
- boto3 clients are instantiated at module scope, correctly reused across warm invocations.
- The README is honest about known issues. That honesty is what made this review tractable — and it is worth noting that every problem the team already suspected turned out to be real and diagnosable from the code. The instincts here are good; the gap is instrumentation and hardening, not understanding.
