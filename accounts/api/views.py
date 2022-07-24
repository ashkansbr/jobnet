from rest_framework import mixins, viewsets
from ..models import Employer, JobSeeker
from .serializers import JobSeekerSerializer, EmployerSerializer
from accounts.api.permissions import IsNotAuthenticated, IsJobSeeker, IsEmployer


class JobSeekerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [IsJobSeeker]


class EmployerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [IsEmployer]

