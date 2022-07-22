from django.db import models
from django.utils.translation import gettext_lazy as _
from common.BaseModel import BaseModel
from address.models import City
from accounts.models import Employer


class CompanyType(BaseModel):
    type = models.CharField(_('type'), unique=True, max_length=150)

    class Meta:
        verbose_name = _('company type')
        verbose_name_plural = _('company types')
        db_table = 'company_type'


class Company(BaseModel):
    persian_name = models.CharField(_('persian name'), max_length=150)
    english_name = models.CharField(_('english name'), max_length=150)
    foundation = models.DateField(verbose_name=_('foundation'))
    site = models.URLField(verbose_name=_('site'), blank=True)
    logo = models.ImageField(upload_to='company/logos/', verbose_name=_('logo'), blank=True, null=True)
    banner = models.ImageField(upload_to='company/banners/', verbose_name=_('banner'), blank=True, null=True)
    type = models.ForeignKey(CompanyType, on_delete=models.PROTECT, verbose_name=_('type'), related_name='companies')
    number_of_employees = models.PositiveSmallIntegerField(verbose_name=_('number of employees'))
    description = models.TextField(verbose_name=_('description'))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='companies', verbose_name=_('city'))
