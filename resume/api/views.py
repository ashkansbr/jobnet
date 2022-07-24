from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from resume.api.serializers import ResumeSerializers
from .permissions import IsJobSeekerOrReadOnly
from resume.models import Resume


class ResumeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializers
    permission_classes = [IsJobSeekerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(job_seeker=self.request.user.job_seeker)
