from rest_framework import viewsets, mixins

from .models import Job
from .serializers import JobSerializer


class JobViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    lookup_field = 'uuid'
    queryset = Job.objects.all()
    serializer_class = JobSerializer

