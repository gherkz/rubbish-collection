import { Box, Typography } from "@mui/material";
import { Address } from "./types"

type Props = {
  address: Address
};

const AddressView = (props: Props) => {
  return (
    <>
      <Typography variant="h6" component="div">
        Address
      </Typography>
      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
        <Typography variant="body1" color="text.secondary" data-testid="street">
          {props.address.street}
        </Typography>
        <Typography variant="body1" color="text.secondary" data-testid="city">
          {props.address.city}
        </Typography>
        <Typography variant="body1" color="text.secondary" data-testid="postcode">
          {props.address.postcode}
        </Typography>
      </Box>
    </>
  );
};

export default AddressView;