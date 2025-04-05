from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestVersionsView(APITestCase):
    def test_version_view_is_correct(self):
        """
        Ensure that the available versions are displayed at the root uri

        """
        url = reverse("available-versions")
        response = self.client.get(url, format="json")

        # ensure that our versions view is the root view
        self.assertEqual(url, "/api/")

        # ensure we get the expected response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"v1alpha1": "http://testserver/api/v1alpha1/"})

        # ensure that all the urls for the different versions return a success response code
        for url in response.data.values():
            response = self.client.get(url, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
