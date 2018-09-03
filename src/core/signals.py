from django.db.models.signals import post_save
from celery import group

from . import models, tasks


def save_job(sender, instance, **kwargs):
    if kwargs.get('created', None):
        urls = [x['url'] for x in instance.urls]
        images = group([tasks.crop_image.s(url) for url in urls])().get(timeout=10)

        instance.urls = [{"url": urls[i], "image": images[i]} for i in range(len(urls))]
        instance.status = models.Job.STATUS_FINISHED

        instance.save()


post_save.connect(save_job, sender=models.Job)