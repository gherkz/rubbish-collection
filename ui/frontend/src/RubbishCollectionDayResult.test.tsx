import { render, screen, fireEvent } from '@testing-library/react';
import RubbishCollectionDayResult from './RubbishCollectionDayResult';
import { Frequency, Results, Status } from './types';
import '@testing-library/jest-dom';

jest.mock('./AddressView', () => () => <div>Mocked AddressView</div>);
jest.mock('./RubbishCollectionDayView', () => () => <div>Mocked RubbishCollectionDayView</div>);

describe('RubbishCollectionDayResult', () => {
  const mockReset = jest.fn();

  const mockResults: Results = {
    address: {
      id: '1',
      street: '1 Station Rd',
      city: 'Cambridge',
      postcode: 'CB1 2JW',
      council: 'Council',
    },
    collectionSchedules: [
      { id: '1', rubbishType: { name: 'General Waste' }, startDate: '2025-01-01', frequency: Frequency.BiWeekly },
      { id: '2', rubbishType: { name: 'Recycling' }, startDate: '2025-01-01', frequency: Frequency.BiWeekly },
    ],
  };
  
  it('should not render anything when status is NotLoaded', () => {
    render(<RubbishCollectionDayResult results={mockResults} status={Status.NotLoaded} onReset={mockReset} />);
    
    expect(screen.queryByText('Mocked AddressView')).not.toBeInTheDocument();
    expect(screen.queryByText('Mocked RubbishCollectionDayView')).not.toBeInTheDocument();
    expect(screen.queryByText('Check another address')).not.toBeInTheDocument();
    expect(screen.queryByText('Address Not Found')).not.toBeInTheDocument();
  });

  it('should render "Address Not Found" when status is NotFound', () => {
    render(<RubbishCollectionDayResult results={mockResults} status={Status.NotFound} onReset={mockReset} />);
    
    expect(screen.getByText('Address Not Found')).toBeInTheDocument();
    expect(screen.queryByText('Mocked AddressView')).not.toBeInTheDocument();
    expect(screen.queryByText('Mocked RubbishCollectionDayView')).not.toBeInTheDocument();
  });


  it('should render address and collection schedule correctly when status is Done', () => {
    render(
      <RubbishCollectionDayResult
        results={mockResults}
        status={Status.Done}
        onReset={mockReset}
      />
    );
    
    expect(screen.getByText('Mocked AddressView')).toBeInTheDocument();
    expect(screen.getByText('Mocked RubbishCollectionDayView')).toBeInTheDocument();
    expect(screen.getByText('Check another address')).toBeInTheDocument();
  });

  it('should call onReset function when the "Check another address" button is clicked', () => {
    render(
      <RubbishCollectionDayResult
        results={mockResults}
        status={Status.Done}
        onReset={mockReset}
      />
    );
    
    const restartButton = screen.getByText('Check another address');
    
    fireEvent.click(restartButton);
    
    expect(mockReset).toHaveBeenCalledTimes(1);
  });
});