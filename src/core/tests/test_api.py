from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core import serializers, models


@override_settings(ROOT_URLCONF='core.urls')
class TestAPI(APITestCase):

    def test_job_serializer(self):
        serialized = serializers.JobSerializer(data={"urls": ["http://foo.com"]})
        serialized.is_valid(raise_exception=True)
        serialized.save()

        self.assertEqual(models.Job.objects.count(), 1)

    def test_api_creates_job(self):
        url = reverse('job-list')
        data = {"urls": ["http://dummyurl.com", "http://foobarurl.com"]}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Job.objects.count(), 1)

        object = models.Job.objects.first()
        self.assertEqual(object.status, models.Job.STATUS_IN_PROGRES)
        self.assertEqual(len(object.urls), 2)

    def test_api_sends_bad_request_on_bad_data(self):
        url = reverse('job-list')
        data = {"urls": []}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_sends_bad_request_on_invalid_urls(self):
        url = reverse('job-list')
        data = {"urls": ["hej.com"]}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
