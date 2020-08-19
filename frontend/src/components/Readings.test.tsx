import React from 'react';
import { render, screen } from '@testing-library/react';
import nock from 'nock';
import Readings from './Readings';

describe('Readings page', () => {
  describe('When user readings data is available', () => {
    beforeEach(() => {
      nock('http://localhost:3001')
        .get('/dev/readings')
        .reply(
          200,
          [{ date: '18/8/20', electricityReading: 1234, gasReading: 2468 }],
          {
            'access-control-allow-origin': '*',
            'access-control-allow-credentials': 'true',
          }
        );

      render(<Readings />);
    });

    describe('Prior to receiving readings data', () => {
      it('displays loading message', async () => {
        const loadingMessage = await screen.getByText(/Loading/i);
        expect(loadingMessage).toBeInTheDocument();
      });
    });

    it('renders headings', async () => {
      const readingDate = await screen.findByText(/Date/i);
      expect(readingDate).toBeInTheDocument();

      const electricReading = await screen.findByText(/Electricity Reading/i);
      expect(electricReading).toBeInTheDocument();

      const gasReading = await screen.findByText(/Gas Reading/i);
      expect(gasReading).toBeInTheDocument();
    });

    it('renders readings', async () => {
      const readingDate = await screen.findByText(/18\/8\/20/i);
      expect(readingDate).toBeInTheDocument();

      const electricReading = await screen.findByText(/1234/i);
      expect(electricReading).toBeInTheDocument();

      const gasReading = await screen.findByText(/2468/i);
      expect(gasReading).toBeInTheDocument();
    });
  });

  describe('When readings API gives an error', () => {
    beforeEach(() => {
      nock('http://localhost:3001').get('/dev/readings').reply(
        500,
        {},
        {
          'access-control-allow-origin': '*',
          'access-control-allow-credentials': 'true',
        }
      );

      render(<Readings />);
    });

    it('renders error view', async () => {
      const readingDate = await screen.findByText(/Failed to fetch readings/i);
      expect(readingDate).toBeInTheDocument();
    });
  });
});
