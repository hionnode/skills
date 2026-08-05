terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "us-east-1"
}

# ---------- knowledge base storage ----------

resource "aws_s3_bucket" "docs" {
  bucket = "acme-support-kb-docs"
}

resource "aws_opensearchserverless_collection" "vectors" {
  name = "acme-support-vectors"
  type = "VECTORSEARCH"
}

resource "aws_bedrockagent_knowledge_base" "support" {
  name     = "acme-support-kb"
  role_arn = aws_iam_role.kb.arn

  knowledge_base_configuration {
    type = "VECTOR"
    vector_knowledge_base_configuration {
      embedding_model_arn = "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0"
    }
  }

  storage_configuration {
    type = "OPENSEARCH_SERVERLESS"
    opensearch_serverless_configuration {
      collection_arn    = aws_opensearchserverless_collection.vectors.arn
      vector_index_name = "support-idx"
      field_mapping {
        vector_field   = "embedding"
        text_field     = "chunk"
        metadata_field = "meta"
      }
    }
  }
}

# ---------- api ----------

resource "aws_lambda_function" "chat" {
  function_name = "acme-support-chat"
  role          = aws_iam_role.lambda.arn
  handler       = "handler.handler"
  runtime       = "python3.12"
  filename      = "../build/chat.zip"
  timeout       = 300
  memory_size   = 1024

  environment {
    variables = {
      KB_ID    = aws_bedrockagent_knowledge_base.support.id
      MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    }
  }
}

resource "aws_apigatewayv2_api" "chat" {
  name          = "acme-support-chat-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_route" "chat" {
  api_id    = aws_apigatewayv2_api.chat.id
  route_key = "POST /chat"
  target    = "integrations/${aws_apigatewayv2_integration.chat.id}"
  # auth handled in the Lambda via a shared API key header
}

resource "aws_apigatewayv2_integration" "chat" {
  api_id           = aws_apigatewayv2_api.chat.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.chat.invoke_arn
}

resource "aws_apigatewayv2_stage" "prod" {
  api_id      = aws_apigatewayv2_api.chat.id
  name        = "prod"
  auto_deploy = true
}

# ---------- iam ----------

resource "aws_iam_role" "lambda" {
  name = "acme-support-chat-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "lambda" {
  role = aws_iam_role.lambda.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["bedrock:*"]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:ListBucket", "s3:PutObject"]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role" "kb" {
  name = "acme-support-kb-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "bedrock.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "kb_admin" {
  role       = aws_iam_role.kb.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonBedrockFullAccess"
}
