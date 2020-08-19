import axios from 'axios';
import { IReading } from '../IReading';

export default function (): Promise<IReading[]> {
  return axios
    .get('http://localhost:3001/dev/readings')
    .then((response) => response.data)
    .catch((err) => {
      throw Error('Failed to fetch readings data');
    });
}
