variable "region_name" {
  default = "eu-west-1"
}
variable "profile_name" {
  default = "p-admin"
}
variable "package_name" {
  default = "lambda.zip"
}
variable "function_name" {
  default = "aws_rds_postgres"
}
variable "handler" {
  default = "aws_rds_postgres.lambda_handler"
}
variable "runtime" {
  default = "python3.7"
}