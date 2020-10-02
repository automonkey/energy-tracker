import axios from 'axios';
import { IReading } from '../IReading';
import fetchConfig from './Config';

export default async function (): Promise<IReading[]> {
  const config = await fetchConfig();

  return axios
    .get(`${config.apiBaseUrl}/readings`)
    .then((response) => response.data)
    .catch((err) => {
      throw Error('Failed to fetch readings data');
    });
}
