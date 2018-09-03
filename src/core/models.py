import uuid

from django.contrib.postgres.fields import ArrayField, HStoreField
from django.db import models


class Job(models.Model):
    STATUS_FINISHED = 0
    STATUS_IN_PROGRES = 1
    STATUS_FAILED = 2

    STATUS_CHOICES = [
        (STATUS_FINISHED, 'Finished'),
        (STATUS_IN_PROGRES, 'In progres'),
        (STATUS_FAILED, 'Failed'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=STATUS_IN_PROGRES)

    """List of all urls and generated images for this job. Following this structure:
    [{url: "http://somescreeshot.url", image: null}, {url: "http://other.url", image: "https://staticpath/image.jpg"}]
    """
    urls = ArrayField(HStoreField())

