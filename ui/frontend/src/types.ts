export type RubbishType = {
  name: string;
}

export enum Frequency {
  Weekly = 'W',
  BiWeekly = 'B'
}

export enum Status {
  NotLoaded = 'NotLoaded',
  NotFound = 'NotFound',
  Done = 'Done',
}

export type CollectionSchedule = {
  id: string;
  rubbishType: RubbishType;
  frequency: Frequency;
  startDate: string;
};

export type Address = {
  id: string;
  street: string;
  city: string;
  postcode: string;
  council: string;
};

export type Results = {
  address: Address;
  collectionSchedules: CollectionSchedule[];
};

export type OnAddressSubmit = (street: string, city: string, postcode: string) => void;
