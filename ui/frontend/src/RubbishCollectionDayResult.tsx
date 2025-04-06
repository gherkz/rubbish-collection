import Button from "@mui/material/Button";
import { Results, Status } from "./types";
import AddressView from "./AddressView";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import RubbishCollectionDayView from "./RubbishCollectionDayView";
import { Typography } from "@mui/material";

type OnReset = () => void;

type Props = {
  results: Results,
  status: Status,
  onReset: OnReset,
};

const RubbishCollectionDayResult = (props: Props) => {
  const reset = () => {
    props.onReset();
  }

  const RestartButton = () => {
    if (props.status === Status.NotLoaded) {
      return <></>;
    }
    return <Button variant="contained" onClick={reset}>Check another address</Button>;
  }

  const Results = () => {
    return (
      <>
        <AddressView address={props.results.address} />
        <RubbishCollectionDayView collectionSchedules={props.results.collectionSchedules} />
      </>
    );
  }

  if (props.status === Status.NotLoaded) {
    return <></>;
  }

  if (props.status === Status.NotFound) {
    return (
      <Typography component="h1" variant="h4" margin='normal'>
        Address Not Found
      </Typography>
    );
  }

  return (
    <Card sx={{ maxWidth: 400, margin: '20px auto', padding: '20px' }}>
      <CardContent>
        <Results />
        <RestartButton />
      </CardContent>
    </Card>
  );
};

export default RubbishCollectionDayResult;