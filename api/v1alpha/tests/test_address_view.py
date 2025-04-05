import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.v1alpha.tests.helpers import addresses_url, create_address


class TestAddressView(APITestCase):

    def test_create_addresses(self):
        address = {
            'street': 'street',
            'city': 'city',
            'postcode': 'postcode',
            'council': 'council',
        }

        response = self.client.post(addresses_url(), address, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': response.data['id'],
            'street': 'street',
            'city': 'city',
            'postcode': 'postcode',
            'council': 'council',
        })

    def test_list_addresses(self):
        expected_address = create_address(self.client, 'street', 'city', 'postcode', 'council')

        response = self.client.get(addresses_url(), format="json", query_params={
            'street': 'street',
            'city': 'city',
            'postcode': 'postcode',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [expected_address])
