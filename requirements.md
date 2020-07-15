# Requirements

> *Last updated: 2020/07/15*

## I. Create free tier account

[https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct&src=header_signup](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct&src=header_signup)

## II. Enable Multi-factor authentication (MFA)

1. Connect to [AWS console](https://aws.amazon.com/fr/console/)
2. Follow the official guide : [https://console.aws.amazon.com/iam/home?#/security_credentials](https://console.aws.amazon.com/iam/home?#/security_credentials)

## III. Create Lambda Deployer user with programmatic access

> https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console

1. Connect to [AWS console](https://aws.amazon.com/fr/console/) with root account
2. Go to **IAM** service
3. Create **Group** named `Lambda_Deployer`
4. Add existing **Policy** `PowerUserAccess` to the group
5. Add existing **Policy** `IAMFullAccess` to the group
6. Create **User** named `lambda-deployer`
7. Check **Programmatic access**
8. Add it to the Lambda_Deployer group 
9. Copy **Access keys** (access key ID and secret access key)
10. Put them in `C:\Users\<User>\.aws/credentials` file, like that:
	```
	[p-lambda-deployer]
	aws_access_key_id = dev_ACCESS_KEY
	aws_secret_access_key = dev_ACCESS_KEY
	region = eu-west-1
	```

### IV. Install **Serverless CLI**
