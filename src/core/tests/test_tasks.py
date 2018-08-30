import mock

from django.test import TestCase
from core import tasks, serializers, models


class TestAPI(TestCase):
    def setUp(self):
        self.serialized = serializers.JobSerializer(data={"urls": [
            "http://example.com",
            "https://example.com",
        ]})
        self.serialized.is_valid(raise_exception=True)

    def test_handle_job_spawns_one_process_for_url(self):
        instance = self.serialized.save()

        result = tasks.handle_job(instance.pk)

        for row in result:
            self.assertEqual(row['url'], row['image'])

