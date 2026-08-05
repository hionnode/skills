---
name: genai-lens-review
description: Review, audit, and design generative AI workloads on AWS against the AWS Well-Architected Framework Generative AI Lens — its six pillars and 51 numbered best practices (GENOPS, GENSEC, GENREL, GENPERF, GENCOST, GENSUS). Use this whenever someone asks for a Well-Architected review of an AI/ML or generative AI system, wants an architecture reviewed before shipping a Bedrock / SageMaker / Amazon Q / agentic workload, asks "is this production-ready", "what are we missing", "audit our RAG pipeline", "review our agent architecture", or wants a gap analysis, risk assessment, or remediation plan for a GenAI system. Also use it proactively when someone is designing a new generative AI workload on AWS (RAG, agents, fine-tuning, model gateways, multi-tenant AI platforms, inference endpoints) — the Lens best practices are exactly the design constraints they should be building against, even if they never say "Well-Architected". Not for non-AWS AI stacks and not for generic AWS reviews that have no generative AI component.
---

# Generative AI Lens review

The AWS Well-Architected Generative AI Lens (2026) defines 51 numbered best practices across six
pillars. Each one carries an AWS-assigned **risk if not established** — High, Medium, or Low. A
review's job is to work out which of those practices apply to the workload in front of you, find
evidence for whether each is actually in place, and report the gaps in risk order with concrete
remediation.

The thing that makes a review worth reading is evidence. A report that says "implement guardrails
to mitigate harmful responses" without pointing at the specific unguarded `InvokeModel` call is
just the whitepaper's table of contents restated. Ground every finding in something you actually
observed — a file and line, a Terraform resource, a console setting the user described, or an
explicit statement from the user that a control doesn't exist.

## What's in this skill

| Path | Contents |
|---|---|
| `assets/best-practices.csv` | All 51 practices: id, pillar, question, title, risk, lifecycle stage. The review's spine. |
| `references/genops.md` | Operational excellence — 10 practices, full guidance and implementation steps |
| `references/gensec.md` | Security — 10 practices |
| `references/genrel.md` | Reliability — 10 practices |
| `references/genperf.md` | Performance efficiency — 8 practices |
| `references/gencost.md` | Cost optimization — 9 practices |
| `references/gensus.md` | Sustainability — 4 practices |
| `references/foundations.md` | Design principles, Responsible AI dimensions, the six lifecycle stages, data architecture, agentic AI patterns, glossary |
| `references/scenarios/*.md` | Eight worked reference architectures (see below) |

The pillar files are large. Read only the pillars in scope, and read them after you know what the
workload is — otherwise you'll spend context on sustainability guidance for a workload that turns
out to be a prototype nobody has deployed.

## The review

### 1. Understand the workload before opening any reference

Build a picture of what you're reviewing. Where there's a repo, IaC, or config to read, read it —
that's stronger evidence than anything the user will type. Look for the things the Lens cares about:

- **Inference surface** — Bedrock, SageMaker endpoints, Amazon Q, self-hosted models, a gateway in
  front of them. On-demand vs. provisioned throughput vs. batch.
- **Data path** — RAG? Which vector store, what chunking and embedding strategy, where the source
  documents live and who can reach them.
- **Agency** — tool calls, agents, multi-step orchestration, anything that can act rather than just
  answer. Agentic workloads pull in a distinct set of practices (GENSEC05, GENREL03-BP02,
  GENCOST05, GENREL05-BP03) that don't apply to a plain completion endpoint.
- **Customization** — prompt engineering only, fine-tuning, continued pre-training, distillation.
- **Controls already present** — guardrails, IAM policies, PrivateLink, prompt catalogs, evaluation
  harnesses, monitoring.
- **Lifecycle stage** — scoping, model selection, model customization, development and integration,
  deployment, or continuous improvement. `foundations.md` describes each. The stage governs which
  practices are fair to assess: holding a scoping-stage design to deployment-stage monitoring
  practices produces noise, not insight.

Ask the user only for what the artifacts can't tell you, and ask in one batch rather than
interrogating them across several turns. Good things to ask: is this in production and for whom,
what data classification flows through it, what's the blast radius if the model says something
wrong, is there a compliance regime in play.

If the workload resembles one of the eight reference scenarios, read that file — it gives you the
architecture AWS would expect and a "lessons learned" list you can compare against:

`multi-tenant-platform` · `autonomous-call-center` · `generative-bi` · `code-transformation` ·
`knowledge-worker-copilot` · `incident-response` · `automated-code-review` · `kanban-workflow`

### 2. Agree the scope

Default to all six pillars — cross-pillar gaps are where the interesting findings live, and a
security-only review will miss that the missing prompt catalog is simultaneously a GENSEC04,
GENREL04 and GENCOST03 problem. But say what you're doing and let the user narrow it. Narrow scopes
worth offering: a single pillar, a single lifecycle stage, or High-risk practices only (22 of the
51) when the user wants a fast triage.

State the scope in the report so nobody reads a security-only review as a clean bill of health.

### 3. Assess each practice in scope

Read `assets/best-practices.csv` for the list, then the pillar reference files for the practices you
need to judge. For each practice, land on one of four verdicts:

- **Met** — evidence shows it's in place. Say what the evidence was; a one-line citation is enough.
- **Partially met** — the control exists but is incomplete or unverified. This is the most common
  honest verdict and the most useful one. Name precisely what's missing.
- **Not met** — no evidence of the control, or the user confirmed it's absent.
- **Not applicable** — the practice genuinely doesn't apply. Justify it, because "not applicable" is
  where reviews quietly go wrong. A workload with no vector store legitimately skips GENPERF04 and
  GENCOST04. A workload that "doesn't need multi-Region" is a business decision the user should make
  explicitly, not something you decide for them — record it as an accepted risk instead.

Where you can't tell, say so. "Insufficient evidence — needs the IAM policy for the Lambda execution
role" is a finding in its own right and far more useful than a guess dressed up as a verdict.

### 4. Rate each gap

The Lens's risk level is *inherent* — how bad it generally is to skip that practice. What matters to
the user is the risk *in their workload*. Start from the Lens rating and adjust for what you learned
in step 1, then say why you adjusted:

- Raise it when the workload amplifies the exposure: PII or regulated data in prompts, external
  end users, agents with write access to production systems, a large uncapped spend surface.
- Lower it when the context contains it: an internal prototype behind SSO with ten users, a
  workload with a hard token budget already enforced upstream.

An adjusted rating with a one-line justification is worth more than a faithful echo of the
whitepaper's number.

### 5. Write the report

Use this structure. It's ordered so that someone who reads only the first page still gets the
decision-relevant part.

```markdown
# Generative AI Lens review — <workload name>

**Reviewed:** <date> · **Scope:** <pillars / lifecycle stage / risk floor>
**Lifecycle stage:** <stage> · **Closest reference scenario:** <scenario or "none">

## Workload summary
<3-5 sentences: what it does, the inference surface, the data path, who uses it.
Enough that a reader who has never seen the system can judge whether the findings land.>

## Assessment at a glance
| Pillar | Met | Partial | Not met | N/A |
|---|---|---|---|---|
<one row per pillar in scope, plus a total row>

## Priority findings
<The gaps that matter, highest adjusted risk first. One block each:>

### <n>. <GENSEC02-BP01> — <practice title>
**Risk:** <adjusted> (Lens: <inherent>) · **Status:** Not met
**Evidence:** <what you observed — file:line, resource name, or the user's own statement>
**Why it matters here:** <the specific consequence for this workload, not the generic one>
**Remediation:** <concrete steps, drawn from the practice's implementation steps but written
against this architecture — actual service names, actual resources>

## Full assessment
<Table of every practice in scope: ID, title, status, risk, one-line evidence. This is the
audit trail; keep the per-row text short since the detail lives above.>

## Accepted risks and exclusions
<Practices marked N/A with justification, and gaps the user has explicitly chosen to accept.>

## Suggested sequence
<Remediation ordered for delivery, not by pillar — group work that touches the same component,
and call out anything that's a prerequisite for something else.>
```

Two habits that make the difference:

**Write remediation against their architecture.** The reference files give implementation steps in
AWS's generic voice. Translate. Not "set up Amazon Bedrock Prompt Management" but "move the five
prompt strings in `src/prompts.py` into Bedrock Prompt Management and pin the Lambda to a version
alias, so a prompt change can be rolled back without a deploy."

**Let the finding count fall where it falls.** A well-built workload might have six findings and
that's a good report. Padding a review with low-value observations to reach some imagined quota
trains the reader to skim, and then they miss the one High that mattered.

## Design mode

When the workload doesn't exist yet, the same practices work as design constraints rather than audit
criteria. The shift: instead of hunting for evidence, walk the lifecycle stages in
`foundations.md` and pull forward the practices that constrain decisions being made *now*. Scoping-
and model-selection-stage practices (GENOPS02-BP03, GENPERF01-BP02, GENCOST02-BP01, GENCOST01-BP01,
GENREL01-BP01, GENSUS01-BP01) are cheap to honor in a design and expensive to retrofit — a model
choice made without a ground-truth evaluation set is very hard to revisit once it's in production.

Read the closest reference scenario and use its architecture as the starting point rather than
inventing one. Then flag which later-stage practices the design should leave room for, so the team
knows what's coming.

## Reference material

The six design principles, the eight Responsible AI dimensions, and the Lens's own definitions are
in `references/foundations.md`. Reach for the design principles when a finding needs framing above
the level of a single practice — "this workload has no controlled-autonomy story at all" is a more
useful headline than nine separate agentic findings.

Full source: the extracted whitepaper text lives at
`/Users/chinmay/code/agency/skills/certification/aws/generative-ai-lens.txt`. Grep it when you need
wording the references condensed away, such as the exact "Related documents" links for a practice.
