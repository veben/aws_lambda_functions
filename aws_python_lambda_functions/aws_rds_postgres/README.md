# Connect to RDS Postgres

> *Last updated: 2020/08/11*
> More information: https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway 

> With Pycharm, mark `aws_rds_postgres` as **Sources Root**

## I. Requirements
An RDS instance with the following parameters:
- Endpoint: "rds-postgres-host.66cezfdpmr.eu-west-1.rds.amazonaws.com"
- Database identifier: "rds-postgres-db"
- Master user: "master"
- Master password: "master-pass"

An Administrator user with programmatic access:
1. Connect to [AWS console](https://aws.amazon.com/fr/console/)
2. Go to **IAM** service
3. Create **Group** named `Administrators`
4. Add existing **Policy** `AdministratorAccess` to the group
5. Create **User** named `admin`
6. Check **Programmatic access**
7. Check **AWS Management Console access** (optional)
8. Add it to the administrator group 
9. Copy **Access keys** (access key ID and secret access key)
10. Put them in `C:\Users\<User>\.aws/credentials` file, like that:
	```
	[p-admin]
	aws_access_key_id = admin_ACCESS_KEY
	aws_secret_access_key = admin_ACCESS_KEY
	region = eu-west-1
	```

## II. Launch unit tests
WIP...

## III. Package
Zip the lambda:
```shell script
zip lambda *.py
```

> Windows version
```shell script
tar.exe -a -c -f lambda.zip *.py
```

## IV. Deployment to AWS with terraform
Init terraform env:
```shell script
terraform init
```
Test the deployment:
```shell script
terraform plan -out "lambda.tfplan"
```
Deploy:
```shell script
terraform apply
```
Destroy:
```shell script
terraform destroy
```

## V. Deployment with Terraform & Github actions
WIP...

## VI. Invoke
WIP...