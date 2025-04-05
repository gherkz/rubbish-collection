import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.v1alpha.tests.helpers import rubbish_types_url, create_rubbish_type


class TestRubbishTypeView(APITestCase):

    def test_create_rubbish_type(self):
        rubbish_type = {
            'name': 'Recycling',
        }

        response = self.client.post(rubbish_types_url(), rubbish_type, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': response.data['id'],
            'name': 'Recycling',
        })

    def test_list_rubbish_types(self):
        recycling_rubbish_type = create_rubbish_type(self.client, 'Recycling')
        general_rubbish_type = create_rubbish_type(self.client, 'General')

        response = self.client.get(rubbish_types_url(), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            recycling_rubbish_type,
            general_rubbish_type
        ])
