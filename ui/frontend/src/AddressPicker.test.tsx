import { render, screen, fireEvent } from '@testing-library/react';
import AddressPicker from './AddressPicker';
import '@testing-library/jest-dom';

const mockSubmit = jest.fn();

describe('AddressPicker', () => {
  beforeEach(() => {
    mockSubmit.mockClear();
  });

  it('renders the form and button correctly', () => {
    render(<AddressPicker submit={mockSubmit} />);

    expect(screen.getByLabelText('Street Address')).toBeInTheDocument();
    expect(screen.getByLabelText('City')).toBeInTheDocument();
    expect(screen.getByLabelText('Postcode')).toBeInTheDocument();
    expect(screen.getByText('Check My Rubbish Collection Day!')).toBeInTheDocument();
  });

  it('submits the form with the correct values when the button is clicked', () => {
    render(<AddressPicker submit={mockSubmit} />);

    const streetInput = screen.getByLabelText('Street Address') as HTMLInputElement;
    const cityInput = screen.getByLabelText('City') as HTMLInputElement;
    const postcodeInput = screen.getByLabelText('Postcode') as HTMLInputElement;
    const submitButton = screen.getByText('Check My Rubbish Collection Day!');

    fireEvent.change(streetInput, { target: { value: '123 Elm Street' } });
    fireEvent.change(cityInput, { target: { value: 'Gotham' } });
    fireEvent.change(postcodeInput, { target: { value: '12345' } });

    fireEvent.click(submitButton);

    expect(mockSubmit).toHaveBeenCalledWith('123 Elm Street', 'Gotham', '12345');
  });
});