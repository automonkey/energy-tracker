import { APIGatewayProxyHandler } from 'aws-lambda';
import 'source-map-support/register';

import { Reading } from './reading';

export const readings: APIGatewayProxyHandler = async () => {
  const readings: Reading[] = [
    { date: "18/8/20", electricityReading: 1234, gasReading: 2468 }
  ];

  return {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': 'http://localhost:3000',
      'Access-Control-Allow-Credentials': false,
    },
    body: JSON.stringify(readings, null, 2),
  };
};
