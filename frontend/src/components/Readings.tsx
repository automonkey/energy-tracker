import React, { useEffect, useState } from 'react';
import './Readings.css';
import fetchReadings from '../services/Readings';
import { IReading } from '../IReading';

function Readings() {
  const [readings, setReadings] = useState<IReading[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let componentUnmounted = false;

    (async function updateReadings() {
      try {
        const fetchedReadings = await fetchReadings();

        if (!componentUnmounted) {
          setReadings(fetchedReadings);
        }
      } catch (err) {
        if (!componentUnmounted) {
          setError('Failed to fetch readings');
        }
      }
    })();

    return function cleanup() {
      componentUnmounted = true;
    };
  }, []);

  return <div className="App">{pageLayout(readings, error)}</div>;
}

function pageLayout(readings: IReading[], error: string | null) {
  if (error) {
    return <p>{error}</p>;
  }

  const isFetchingData = readings.length === 0 && !error;
  if (isFetchingData) {
    return <p>Loading...</p>;
  }

  return readingsView(readings);
}

function readingsView(readings: IReading[]) {
  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Electricity Reading</th>
          <th>Gas Reading</th>
        </tr>
      </thead>
      <tbody>
        {readings.map((reading) => (
          <tr key={reading.date}>
            <td>{reading.date}</td>
            <td>{reading.electricityReading}</td>
            <td>{reading.gasReading}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Readings;
