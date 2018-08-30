from celery import group
from screenshotr.celery import app
from .models import Job


@app.task
def handle_job(pk):
    instance = Job.objects.get(pk=pk)

    urls = [x['url'] for x in instance.urls]
    images = group([crop_image.s(url) for url in urls])().get()

    return [{"url": urls[i], "image": images[i]} for i in range(len(urls))]


@app.task
def crop_image(url):
    return url