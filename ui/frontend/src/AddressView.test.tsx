import '@testing-library/jest-dom';

import { render, screen } from '@testing-library/react';
import AddressView from './AddressView';
import { Address } from './types';

describe('AddressView', () => {
  it('renders the address correctly', () => {
    const address: Address = {
      id: '1',
      street: 'street',
      city: 'city',
      postcode: 'postcode',
      council: 'council',
    }

    render(<AddressView address={address} />);

    expect(screen.getByTestId('street')).toHaveTextContent('street');
    expect(screen.getByTestId('city')).toHaveTextContent('city');
    expect(screen.getByTestId('postcode')).toHaveTextContent('postcode');
  });
});