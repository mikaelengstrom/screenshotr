from django.urls import reverse
from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError
from django.core.validators import URLValidator

from . import models


class URLSField(serializers.ListField):
    def to_internal_value(self, data):
        if len(data) < 1:
            raise ValidationError('No URLS specified')

        assert_is_valid = URLValidator()
        for x in data:
            assert_is_valid(x)

        return [{"url": x, "image": None} for x in data]


class JobSerializer(serializers.ModelSerializer):
    urls = URLSField()
    status = serializers.ReadOnlyField(source='get_status_display')
    job_url = serializers.SerializerMethodField()

    def get_job_url(self, instance):
        return reverse('job-detail', kwargs={'uuid': instance.uuid})

    class Meta:
        model = models.Job

        fields = (
            'uuid',
            'created',
            'status',
            'job_url',
            'urls',
        )
        read_only = (
            'uuid',
            'created',
            'status',
        )