from django.contrib import admin
from .models import Product, BaseProduct
# Register your models here.
@admin.register(BaseProduct)
class BaseProductAdmin(admin.ModelAdmin):
    model = BaseProduct
    list_display = (
        'uuid',
        'name'
    )
    list_filter = (
        'category',
        'active_ingredient',
        'manufacturer',
        'brand',
        'route_of_administration',
        'medicine_physical_state',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'uuid',
        'base_product',
        'stock'
    )
    list_filter = (
        'base_product',
        'merchant',
        'stock',
        'active',
        ('deleted_at',admin.EmptyFieldListFilter)
    )
