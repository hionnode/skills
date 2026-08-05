"""Customer support chat endpoint.

POST /chat  {"question": "...", "customer_id": "..."}
Retrieves from the Bedrock knowledge base, then answers with Claude.
"""
import json
import os

import boto3

bedrock = boto3.client("bedrock-runtime")
agent = boto3.client("bedrock-agent-runtime")

KB_ID = os.environ["KB_ID"]
MODEL_ID = os.environ["MODEL_ID"]
API_KEY = "sk-acme-support-2f8a91"

SYSTEM_PROMPT = """You are Acme's customer support assistant.
Answer the customer's question using the context below. Be thorough and helpful.
You have access to the customer's full account history, billing records and open tickets.
If the context does not contain the answer, use your general knowledge to help anyway.

Context:
{context}
"""


def retrieve(question):
    resp = agent.retrieve(
        knowledgeBaseId=KB_ID,
        retrievalQuery={"text": question},
        retrievalConfiguration={
            "vectorSearchConfiguration": {"numberOfResults": 20}
        },
    )
    return "\n\n".join(r["content"]["text"] for r in resp["retrievalResults"])


def handler(event, context):
    if event.get("headers", {}).get("x-api-key") != API_KEY:
        return {"statusCode": 401, "body": "unauthorized"}

    body = json.loads(event["body"])
    question = body["question"]

    ctx = retrieve(question)

    resp = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4096,
                "temperature": 0.9,
                "system": SYSTEM_PROMPT.format(context=ctx),
                "messages": [{"role": "user", "content": question}],
            }
        ),
    )

    answer = json.loads(resp["body"].read())["content"][0]["text"]
    return {"statusCode": 200, "body": json.dumps({"answer": answer})}
