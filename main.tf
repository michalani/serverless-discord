# Deploys a serverless discord bot resources in AWS

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-west-1"
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "serverless-discord-iam-role" {
  name               = "serverless-discord-iam-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda" {
  type        = "zip"
  source_file = "main.py"
  output_path = "serverless-discord.zip"
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "pynacl-layer.zip"
  layer_name = "pynacl-layer"

  compatible_runtimes = ["python3.8"]
}

# lambda function
resource "aws_lambda_function" "serverless-discord-lambda-function" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "serverless-discord.zip"
  function_name = "serverless-discord"
  role          = aws_iam_role.serverless-discord-iam-role.arn
  handler       = "main.lambda_handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.8"

  layers = [aws_lambda_layer_version.lambda_layer.arn]

  environment {
    variables = {
      DISCORD_PUBLIC_KEY = local.envs["DISCORD_PUBLIC_KEY"]
    }
  }
}

resource "aws_apigatewayv2_api" "apigw" {
  name          = "serverless-discord"
  protocol_type = "HTTP"
  target = aws_lambda_function.serverless-discord-lambda-function.arn
  route_key = "POST /interactions"
}

resource "aws_lambda_permission" "apigw" {
	action        = "lambda:InvokeFunction"
	function_name = aws_lambda_function.serverless-discord-lambda-function.arn
	principal     = "apigateway.amazonaws.com"
  
	source_arn = "${aws_apigatewayv2_api.apigw.execution_arn}/*/*"
}

resource "aws_apigatewayv2_integration" "example" {
  api_id           = aws_apigatewayv2_api.apigw.id
  integration_type = "AWS_PROXY"

  connection_type           = "INTERNET"
  description               = "Lambda example"
  integration_method        = "POST"
  integration_uri           = aws_lambda_function.serverless-discord-lambda-function.arn
  passthrough_behavior      = "WHEN_NO_MATCH"
}

output "InteractionsEndpointURL" {
  # value = aws_apigatewayv2_api.apigw.api_endpoint+""
  value = "${aws_apigatewayv2_api.apigw.api_endpoint}${local.envs["ENDPOINT_PATH"]}"
  sensitive = true
}