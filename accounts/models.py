from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from common.BaseModel import BaseModel


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator

    username = models.CharField(_('username'), max_length=150, unique=True,
                                help_text=_('Required 150 character or fewer letters, digits and @/./+/-/_ only'),
                                error_messages={'unique': 'a user with this username is already exist'})

    email = models.EmailField(_('email address'), unique=True)
    email_verified = models.BooleanField(default=False, verbose_name=_('email verified'))
    phone_number = models.CharField(_('phone number'), max_length=11, blank=True)
    is_employer = models.BooleanField(default=False, verbose_name=_('is employer'))
    is_job_seeker = models.BooleanField(default=False, verbose_name=_('is job seeker'))

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'


class Employer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='employer')

    class Meta:
        verbose_name = _('employer')
        verbose_name_plural = _('employers')
        db_table = 'employer'


class JobSeeker(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'), related_name='job_seeker')
    birth_day = models.DateField(_('birth day'), blank=True, null=True)

    class Meta:
        verbose_name = _('job seeker')
        verbose_name_plural = _('job seekers')
        db_table = 'job_seeker'
