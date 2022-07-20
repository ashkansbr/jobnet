from django.db import models
from common.BaseModel import BaseModel
from django.utils.translation import gettext_lazy as _


class Province(BaseModel):
    name = models.CharField(_('name'), max_length=50, unique=True)
    slug = models.SlugField(_('slug'), unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(_('name'), unique=True, max_length=150)
    slug = models.SlugField(_('slug'), unique=True, max_length=150)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name


