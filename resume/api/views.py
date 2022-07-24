from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from resume.api.serializers import ResumeSerializers
from resume.models import Resume


class ResumeViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializers

    def perform_create(self, serializer):
        serializer.save(job_seeker=self.request.user.job_seeker)
