from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import JobSeeker, Employer
from address.models import City
from resume.models import Resume
from common.BaseModel import BaseModel
from company.models import Company


class JobCategory(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('job category')
        verbose_name_plural = _('job categories')
        db_table = 'job_category'


class Skill(BaseModel):
    title = models.CharField(max_length=150, verbose_name=_('title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        db_table = 'skill'


class Job(BaseModel):
    class WorkExperienceChoices(models.TextChoices):
        NOT_IMPORTANT = '0', _('not important')
        LESS_THAN_THREE = '1', _('less than three years')
        BETWEEN_THREE_AND_SIX = '2', _('between three and six years')
        MORE_THAN_SIX = '3', _('more than six years')

    class CooperationChoices(models.TextChoices):
        FULL_TIME = '0', _('full time')
        PART_TIME = '1', _('part time')

    class GenderChoices(models.TextChoices):
        MALE = '0', _('male')
        FEMALE = '1', _('female')

    class DegreeChoices(models.TextChoices):
        ASSOCIATED = '0', _('associate')
        BACHELOR = '1', _('bachelor')
        NOT_IMPORTANT = '2', _('not important')

    class ServedOrExemptChoices(models.TextChoices):
        NOT_IMPORTANT = '0', _('not important')
        SERVED_OR_EXEMPT = '1', _('served or exempt')

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs', verbose_name=_('employer'))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs', verbose_name=_('company'))
    title = models.CharField(max_length=150, verbose_name=_('title'))
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, related_name='jobs',
                                 null=True, verbose_name=_('category'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_('city'), related_name='jobs')
    cooperation_type = models.CharField(choices=CooperationChoices.choices, verbose_name=_('cooperation type'),
                                        max_length=1)
    work_experience = models.CharField(max_length=1, choices=WorkExperienceChoices.choices,
                                       verbose_name=_('work experience'))
    Gender = models.CharField(choices=GenderChoices.choices, max_length=1, verbose_name=_('gender'))
    degree = models.CharField(choices=DegreeChoices.choices, max_length=1, verbose_name=_('degree'))
    salary = models.PositiveIntegerField(verbose_name=_('salary'), null=True)
    required_skills = models.ManyToManyField(Skill, verbose_name=_('skill'), related_name='jobs')
    military_status = models.CharField(max_length=1, choices=ServedOrExemptChoices.choices,
                                       verbose_name=_('military status'))

    def __str__(self):
        return f"{self.title}{self.company.name}"

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')
        db_table = 'job'


class JobRequest(BaseModel):
    class SeenStatusChoices(models.TextChoices):
        SEEN = '0', _('seen')
        NOT_SEEN = '1', _('not seen')

    class StatusChoices(models.TextChoices):
        WAITING = '0', _('waiting')
        DENIED = '1', _('denied')

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_request', verbose_name=_('job'))
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.PROTECT, related_name='job_request',
                                   verbose_name=_('job seeker'))
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, related_name='job_request',
                               verbose_name=_('resume'))
    seen_status = models.CharField(max_length=1, choices=SeenStatusChoices.choices, verbose_name=_('seen status'))
    status = models.CharField(choices=StatusChoices.choices, max_length=1, verbose_name=_('status'))

    class Meta:
        verbose_name = _('job request')
        verbose_name_plural = _('job requests')
        db_table = 'job_request'
