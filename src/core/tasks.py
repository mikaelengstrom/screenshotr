import imgkit

from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings

from screenshotr.celery import app


@app.task
def crop_image(url):
    file_name = generate_file_name(url)
    path = settings.MEDIA_ROOT + file_name

    res = imgkit.from_url(url, path , options={'xvfb': ''})
    if res:
        return settings.MEDIA_URL + file_name


def generate_file_name(url):
    return slugify("{}-{}".format(url, timezone.now())) + '.jpg'
