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
    introduction = models.TextField(verbose_name=_('introduction'))
    culture = models.TextField(verbose_name=_('culture'))
    advantages = models.TextField(verbose_name=_('advantages'))
    employer = models.OneToOneField(Employer, on_delete=models.CASCADE, verbose_name=_('employer'),
                                    related_name='company')

    @property
    def name(self):
        return f"{self.persian_name} | {self.english_name}"

    def __str__(self):
        return self.name


class EmployeeType(BaseModel):
    type = models.CharField(_('type'), max_length=150)

    def __str__(self):
        return self.type


class Employee(BaseModel):
    name = models.CharField(_('name'), max_length=150, )
    image = models.ImageField(upload_to='employee/images/', verbose_name=_('images'))
    description = models.TextField(verbose_name=_('description'))
    type = models.ForeignKey(EmployeeType, verbose_name=_('type'), on_delete=models.PROTECT, related_name='employees')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', verbose_name=_('company'))

    def __str__(self):
        return f"{self.name} | {self.type}"

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employee'
