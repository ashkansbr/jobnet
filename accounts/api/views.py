from rest_framework import mixins, viewsets
from ..models import Employer, JobSeeker
from .serializers import JobSeekerSerializer, EmployerSerializer


class JobSeekerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer


class EmployerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

