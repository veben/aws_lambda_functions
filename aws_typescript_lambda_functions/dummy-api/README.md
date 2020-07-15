# Typescript lambda deployment

> *Last updated: 2020/07/15*

1. Generate typescript lambda template
```shell script
sls create -t aws-nodejs-typescript
```
2. Install AWS SDK
```shell script
npm i aws-sdk
```
3. Install plugin **serverless-offline**
```shell script
npm i --save-dev serverless-offline
```
4. Install plugin **serverless-prune-plugin**
```shell script
npm i --save-dev serverless-prune-plugin
```
5. Deploy function
```shell script
sls deploy --aws-profile p-lambda-deployer --verbose
```
6. Remove function
```shell script
sls remove --aws-profile p-lambda-deployer --verbose
```