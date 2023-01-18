from dirtyfields import DirtyFieldsMixin
from django.db import models
from autoslug import AutoSlugField

from pharmaco_backend.utils import PreModel


# Create your models here.
class Category(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=100, verbose_name='Category name')
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='subcategories')

    def __str__(self):
        return self.name


# class Attribute(DirtyFieldsMixin, PreModel):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name

class Brand(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class Ingredient(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class Supplier(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class MedicinePhysicalState(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class RouteOfAdministration(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', editable=False, unique=True)

    def __str__(self):
        return self.name


class PoliceStation(DirtyFieldsMixin, PreModel):
    name = models.CharField(max_length=255)
