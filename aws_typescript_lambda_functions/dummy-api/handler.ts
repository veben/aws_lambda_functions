import { APIGatewayProxyHandler } from 'aws-lambda';
import 'source-map-support/register';

export const dummy_api: APIGatewayProxyHandler = async (event, _context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Your dummy api executed successfully!',
      input: event,
    }, null, 2),
  };
}
