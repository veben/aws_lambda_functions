terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = var.region_name
  profile = var.profile_name
}

resource "aws_lambda_function" "aws_rds_postgres" {
  function_name = var.function_name

  filename = var.package_name
  source_code_hash = filebase64sha256(var.package_name)

  handler = var.handler
  runtime = var.runtime

  role = aws_iam_role.lambda_init_postgres_role.arn
}

resource "aws_iam_role" "lambda_init_postgres_role" {
  name               = "lambda_init_postgres_role"
  description        = "Role for Lambda that will update the target group."
  assume_role_policy = data.aws_iam_policy_document.lambda_init_postgres_assume_role_policy_document.json
}

data "aws_iam_policy_document" "lambda_init_postgres_assume_role_policy_document" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}