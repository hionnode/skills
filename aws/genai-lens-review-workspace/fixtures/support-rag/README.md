# Acme customer support assistant

RAG chat assistant for Acme's customer support portal. Customers ask billing and
product questions in the support widget; the assistant answers from our help-centre
articles plus the customer's own account records.

## Status

Live in `us-east-1` since March. Roughly 40k conversations/month, growing ~15%
month over month. Serves external customers directly — the widget is embedded on
the public support site.

## Architecture

- API Gateway (HTTP API) → Lambda → Bedrock
- Bedrock Knowledge Base over OpenSearch Serverless, source docs in S3
- Help-centre articles are re-synced to the KB nightly by a separate cron Lambda
- Account records (billing history, open tickets, plan tier) are exported into the
  same S3 bucket by the billing team's ETL job

## Known issues

- Latency spikes to 20s+ under load, occasional 429s from Bedrock
- Bedrock spend has roughly tripled since launch and nobody can explain the shape
  of the bill
- Support leads say answers are "confidently wrong" maybe 1 in 20 times, but we
  don't have a way to measure this
- One incident where the assistant surfaced another customer's ticket summary

## Deploy

```
cd infra && terraform apply
```
