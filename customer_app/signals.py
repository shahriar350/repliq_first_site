from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from customer_app.models import Cart, Checkout, CheckoutDeliveryStatus
from pharmaco_backend.utils import create_slug


@receiver(pre_save, sender=Checkout)
def update_cart_active_when_checkout_created(sender, instance, **kwargs):
    if instance.pk is None:
        instance.cart.active = False
        instance.cart.deleted_at = timezone.now()
        instance.cart.save()


@receiver(post_save, sender=Checkout)
def create(sender, instance, created, **kwargs):
    if created:
        instance.cart.completed = True
        instance.cart.save()
        if not CheckoutDeliveryStatus.objects.filter(Q(checkout=instance) & Q(status=0)).exists():
            CheckoutDeliveryStatus.objects.create(
                checkout=instance,
                status=0
            )
