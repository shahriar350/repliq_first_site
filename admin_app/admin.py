from django.contrib import admin
from .models import Category,Brand,Supplier,Ingredient,Manufacturer,MedicinePhysicalState,RouteOfAdministration
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = (
        'uuid',
        'name',
        'parent',
        'updated_at',
    )

    list_filter = (
        'name',
        'parent',
        'active',
        ('deleted_at', admin.EmptyFieldListFilter)
    )

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(MedicinePhysicalState)
class MedicinePhysicalStateAdmin(admin.ModelAdmin):
    model = MedicinePhysicalState
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(RouteOfAdministration)
class RouteOfAdministrationAdmin(admin.ModelAdmin):
    model = RouteOfAdministration
    list_display = (
        'uuid',
        'name',
        'updated_at',
    )

    list_filter = (
        'name',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )