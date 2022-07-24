from django.db import models
from django.utils.translation import gettext_lazy as _
from common.BaseModel import BaseModel
from accounts.models import JobSeeker


class Resume(BaseModel):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, verbose_name=_('job seeker'),
                                   related_name='resumes')
    file = models.FileField(upload_to='resumes/', verbose_name=_('file'))

    def __str__(self):
        return self.file.url

    class Meta:
        verbose_name = _('resume')
        verbose_name_plural = _('resumes')
        db_table = 'resume'
