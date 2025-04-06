import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { FormEvent } from 'react';
import { OnAddressSubmit } from './types';

const AddressPicker = (props: {submit: OnAddressSubmit}) => {
  const submitAddress = (e: FormEvent) => {
    e.preventDefault();

    const street = document.getElementById('street') as HTMLInputElement;
    const city = document.getElementById('city') as HTMLInputElement;
    const postcode = document.getElementById('postcode') as HTMLInputElement;

    props.submit(street.value, city.value, postcode.value);
  }

  return (
    <Card sx={{ maxWidth: 400, margin: '20px auto', padding: '20px' }}>
      <CardContent>
        <form onSubmit={submitAddress}>
          <Typography component="h1" variant="h4">
            Address Lookup
          </Typography>
          <FormControl margin="normal" fullWidth>
            <FormLabel htmlFor="street">Street Address</FormLabel>
            <TextField autoComplete="address-line1" required id="street" fullWidth />
          </FormControl>
          <FormControl margin="normal" fullWidth>
            <FormLabel htmlFor="city">City</FormLabel>
            <TextField autoComplete="address-level2" required id="city" fullWidth />
          </FormControl>
          <FormControl margin="normal" fullWidth>
            <FormLabel htmlFor="postcode">Postcode</FormLabel>
            <TextField autoComplete="postal-code" required id="postcode" fullWidth />
          </FormControl>
          <Button type="submit" variant="contained" fullWidth>
            Check My Rubbish Collection Day!
          </Button>
        </form>
      </CardContent>
    </Card>
  )
};

export default AddressPicker;
