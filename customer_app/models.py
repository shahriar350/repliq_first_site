import uuid

from dirtyfields import DirtyFieldsMixin
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from auth_app.models import UserAddress
from pharmaco_backend.utils import PreModel
from product_app.models import Product
from autoslug import AutoSlugField

User = get_user_model()


# Create your models here.
class Cart(DirtyFieldsMixin, PreModel):
    customer = models.ForeignKey(User, related_name="get_customer_carts", on_delete=models.CASCADE)
    slug = AutoSlugField(unique_with='customer__name',editable=False,unique=True)

    @property
    def get_customer_name(self):
        return self.customer.name


class CartProduct(DirtyFieldsMixin, PreModel):
    cart = models.ForeignKey(Cart, related_name='get_cart_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="get_product_carts", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.product.base_product.name


class Checkout(DirtyFieldsMixin, PreModel):
    slug = AutoSlugField(unique_with='customer__name',editable=False,unique=True)
    customer = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='user_checkouts')
    cart = models.ForeignKey(Cart, blank=True, on_delete=models.CASCADE, related_name='cart_checkout')
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    location = models.ForeignKey(UserAddress, on_delete=models.CASCADE, related_name="user_address_checkouts")
    completed = models.BooleanField(default=False)


class CheckoutProduct(DirtyFieldsMixin, PreModel):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='get_checkout_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='get_product_checkouts')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(1)])


class CheckoutDeliveryStatus(DirtyFieldsMixin, PreModel):
    status_choices = (
        (0, 'Order placed'),
        (1, 'Processing'),
        (2, 'Packaging'),
        (3, 'On-way'),
        (4, 'Reached'),
        (5, 'Completed'),
    )
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='get_checkout_delivery_status')
    status = models.PositiveSmallIntegerField(default=0, choices=status_choices)
