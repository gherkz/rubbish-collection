import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import RubbishCollectionDay from './RubbishCollectionDay';
import { Address, CollectionSchedule, Frequency, OnAddressSubmit, Status } from './types';
import '@testing-library/jest-dom';

jest.mock('./AddressPicker', () => (props: {submit: OnAddressSubmit}) => {
  const onClick = (_: React.MouseEvent<HTMLElement>) => {
    props.submit('street', 'city', 'postcode');
  }

  return <div>
    <span>Mocked AddressPicker</span>
    <button onClick={onClick} data-testid="submit-button">Submit</button>
  </div>
});

jest.mock('./RubbishCollectionDayResult', () => (props: {status: Status, onReset: () => void}) => {
  const onClick = (_: React.MouseEvent<HTMLElement>) => {
    props.onReset();
  }

  return <div>
    <span data-testid="status">Mocked RubbishCollectionDayResult - {props.status}</span>
    <button onClick={onClick} data-testid="reset-button">Reset</button>
  </div>
});

const mockedFetch = jest.fn();
global.fetch = mockedFetch;

describe('RubbishCollectionDay Component', () => {
  const mockAddress: Address = { id: '1', street: 'Test Street', city: 'Test City', postcode: '12345', council: 'Council' };
  const mockCollectionSchedules: CollectionSchedule[] = [
    { id: '1', rubbishType: { name: 'Recycling' }, frequency: Frequency.BiWeekly, startDate: '2025-01-01' },
    { id: '2', rubbishType: { name: 'General Waste' }, frequency: Frequency.BiWeekly, startDate: '2025-01-08' },
  ];

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('should render AddressPicker when the status is NotLoaded', () => {
    render(<RubbishCollectionDay />);
    expect(screen.getByText('Mocked AddressPicker')).toBeInTheDocument();
  });

  it('should fetch and display results when valid address is provided', async () => {
    mockedFetch.mockResolvedValueOnce({
      json: () => Promise.resolve([mockAddress]),
    });

    mockedFetch.mockResolvedValueOnce({
      json: () => Promise.resolve(mockCollectionSchedules),
    });

    render(<RubbishCollectionDay />);

    fireEvent.click(screen.getByTestId('submit-button'));

    await waitFor(() => {
      expect(screen.getByTestId('status')).toHaveTextContent('Mocked RubbishCollectionDayResult - Done');
    });

    expect(screen.queryByText('Mocked AddressPicker')).not.toBeInTheDocument();
  });

  it('should display a not found message if address is not found', async () => {
    mockedFetch.mockResolvedValueOnce({
      json: () => Promise.resolve([]),
    });

    render(<RubbishCollectionDay />);

    fireEvent.click(screen.getByTestId('submit-button'));

    await waitFor(() => {
      expect(screen.getByTestId('status')).toHaveTextContent('Mocked RubbishCollectionDayResult - NotFound');
    });
  });

  it('should reset the state when the restart button is clicked', async () => {
    mockedFetch.mockResolvedValueOnce({
      json: () => Promise.resolve([mockAddress]),
    });
    mockedFetch.mockResolvedValueOnce({
      json: () => Promise.resolve(mockCollectionSchedules),
    });

    render(<RubbishCollectionDay />);

    fireEvent.click(screen.getByTestId('submit-button'));

    await waitFor(() => {
      expect(screen.getByTestId('status')).toHaveTextContent('Mocked RubbishCollectionDayResult - Done');
    });

    fireEvent.click(screen.getByTestId('reset-button'));

    await waitFor(() => {
      expect(screen.getByText('Mocked AddressPicker')).toBeInTheDocument();
    });
  });
});
