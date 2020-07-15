import { Serverless } from 'serverless/aws';

const serverlessConfiguration: Serverless = {
    service: {
        name: 'dummy-api',
    },
    frameworkVersion: '>=1.72.0',
    custom: {
        webpack: {
            webpackConfig: './webpack.config.js',
            includeModules: true,
        },
    },
    plugins: [
        'serverless-webpack',
        'serverless-offline',
        'serverless-prune-plugin'
    ],
    provider: {
        name: 'aws',
        runtime: 'nodejs12.x',
        apiGateway: {
            minimumCompressionSize: 1024,
        },
        environment: {
            AWS_NODEJS_CONNECTION_REUSE_ENABLED: '1',
        },
    },
    functions: {
        dummy_api: {
            handler: 'handler.dummy_api',
            events: [
                {
                    http: {
                        method: 'get',
                        path: 'dummy_api',
                    },
                },
            ],
        },
    },
};

module.exports = serverlessConfiguration;
