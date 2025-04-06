import React, { useEffect, useState } from 'react';
import './App.css';
import AddressPicker from './AddressPicker';
import { Address, Results, CollectionSchedule, Status } from './types';
import RubbishCollectionDayResult from './RubbishCollectionDayResult';

const RubbishCollectionDay = () => {
  const [street, setStreet] = useState('');
  const [city, setCity] = useState('');
  const [postcode, setPostcode] = useState('');
  const [status, setStatus] = useState(Status.NotLoaded);
  const [result, setResult] = useState({} as Results);

  useEffect(() => {
    const fetchAddress = async (street: string, city: string, postcode: string) => {
      const url = new URL('/api/v1alpha1/addresses/', window.location.href);
      url.searchParams.append('street', street);
      url.searchParams.append('city', city);
      url.searchParams.append('postcode', postcode);

      const response = await fetch(url);
      const responseJson = await response.json();

      if (responseJson.length > 0) {
        return responseJson[0] as Address;
      }
      
      return null;
    };

    const fetchCollectionSchedules = async (addressId: string) => {
      const encodedAddressId = encodeURIComponent(addressId);
      const url = new URL(`/api/v1alpha1/addresses/${encodedAddressId}/collection-schedules`, window.location.href);
  
      const response = await fetch(url);
      return await response.json() as CollectionSchedule[];
    };

    const fetchData = async () => {
      setResult({} as Results);
      setStatus(Status.NotLoaded);

      if (street && city && postcode) {
        const address = await fetchAddress(street, city, postcode);

        if (address) {
          const collectionSchedules = await fetchCollectionSchedules(address.id);
          setResult({
            address,
            collectionSchedules,
          });
          setStatus(Status.Done);
        } else {
          setResult({} as Results);
          setStatus(Status.NotFound);
        }
      }
    };

    fetchData();
  }, [street, city, postcode]);

  const handleAddressSubmission = (street: string, city: string, postcode: string) => {
    setStreet(street);
    setCity(city);
    setPostcode(postcode);
  };

  const restart = () => {
    setStreet('');
    setCity('');
    setPostcode('');
    setResult({} as Results);
    setStatus(Status.NotLoaded);
  };

  return (
    <div>
      { status === Status.NotLoaded ? <AddressPicker submit={handleAddressSubmission} /> : <></> }
      <RubbishCollectionDayResult results={result} status={status} onReset={restart} />
    </div>
  );
};

export default RubbishCollectionDay;
