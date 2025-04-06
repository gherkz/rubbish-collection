import { Box, Typography } from "@mui/material";
import { CollectionSchedule, Frequency } from "./types"
import { DateTime } from "luxon";

type Props = {
  collectionSchedules: CollectionSchedule[]
};

const RubbishCollectionDayView = (props: Props) => {
  const frequencyDays = {
    [Frequency.Weekly]: 7,
    [Frequency.BiWeekly]: 14,
  };

  const getNextScheduleAfterToday = (collectionSchedule: CollectionSchedule) => {
    const start = DateTime.fromFormat(collectionSchedule.startDate, 'yyyy-MM-dd', { zone: 'local' });
    const today = DateTime.local();

    const daysDiff = today.diff(start, 'days').days;

    const daysBetweenCollections = frequencyDays[collectionSchedule.frequency];
    const nextEventDate = start.plus({ days: Math.ceil(daysDiff / daysBetweenCollections) * daysBetweenCollections });

    return nextEventDate.toLocaleString();
  }

  const schedules = props.collectionSchedules.map(collectionSchedule => {
    const nextCollectionDate = getNextScheduleAfterToday(collectionSchedule);

    return (
      <Box sx={{ display: 'flex', flexDirection: 'column' }} margin='normal' key={collectionSchedule.rubbishType.name}>
        <Typography variant="h6" component="div">
          {collectionSchedule.rubbishType.name}
        </Typography>
        <span data-testid={collectionSchedule.id}>
          Your {collectionSchedule.rubbishType.name} rubbish will next be collected on {nextCollectionDate}
        </span>
      </Box>
    );
  });

  return (
    <>
      {schedules}
    </>
  );
}

export default RubbishCollectionDayView;