import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.v1alpha.tests.helpers import collection_schedules_url, create_collection_schedule, \
    create_rubbish_type, create_address


class TestCollectionScheduleView(APITestCase):

    def test_create_collection_schedules(self):
        address = create_address(self.client, 'street', 'city', 'postcode', 'council')
        create_rubbish_type(self.client, 'General')
        collection_schedule = {
            'rubbish_type': {'name': 'General'},
            'frequency': 'B',
            'start_date': '2025-01-01',
        }

        response = self.client.post(collection_schedules_url(address['id']), collection_schedule, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': response.data['id'],
            'rubbish_type': {'name': 'General'},
            'frequency': 'B',
            'start_date': '2025-01-01',
            'import_date': response.data['import_date']
        })

    def test_list_collection_schedules(self):
        general_rubbish_type = create_rubbish_type(self.client, 'General')
        recycling_rubbish_type = create_rubbish_type(self.client, 'Recycling')
        address = create_address(self.client, 'street', 'city', 'postcode', 'council')
        general_collection_schedule = create_collection_schedule(
            self.client,
            address['id'],
            general_rubbish_type,
            'B',
            '2025-01-01'
        )
        recycling_collection_schedule = create_collection_schedule(
            self.client,
            address['id'],
            recycling_rubbish_type,
            'B',
            '2025-01-01'
        )

        response = self.client.get(collection_schedules_url(address['id']), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            general_collection_schedule,
            recycling_collection_schedule
        ])
