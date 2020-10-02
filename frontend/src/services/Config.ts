import axios from 'axios';

interface Config {
  apiBaseUrl: string;
}

let config: Config | null = null;

export default function (): Promise<Config> {
  if (!config) {
    return axios
      .get('/config.json')
      .then((response) => {
        config = response.data;
        return response.data;
      })
      .catch(() => {
        throw Error('Failed to fetch application config');
      });
  }

  return Promise.resolve(config);
}
