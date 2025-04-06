import '@testing-library/jest-dom';

import { render, screen } from '@testing-library/react';
import { DateTime, Settings } from 'luxon';
import RubbishCollectionDayView from './RubbishCollectionDayView';
import { CollectionSchedule, Frequency } from './types';

describe('RubbishCollectionDayView', () => {
  const collectionSchedules: CollectionSchedule[] = [
    {
      id: '1',
      rubbishType: { name: 'General Waste' },
      startDate: '2025-01-01',
      frequency: Frequency.BiWeekly,
    },
    {
      id: '2',
      rubbishType: { name: 'Recycling' },
      startDate: '2025-01-08',
      frequency: Frequency.BiWeekly,
    },
  ];

  beforeEach(() => {
    const now = DateTime.local(2025, 4, 2, 0, 0, 0);
    Settings.now = () => now.toMillis();
    Settings.defaultLocale = 'en-gb';
  });

  it('renders the next collection dates correctly', () => {
    render(<RubbishCollectionDayView collectionSchedules={collectionSchedules} />);

    expect(screen.getByTestId('1')).toHaveTextContent('Your General Waste rubbish will next be collected on 09/04/2025');
    expect(screen.getByTestId('2')).toHaveTextContent('Your Recycling rubbish will next be collected on 02/04/2025');
  });
});