# Generated by Django 4.1.5 on 2023-01-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkout',
            name='payment_method',
            field=models.SmallIntegerField(choices=[(0, 'Cash On Delivery')], default=1),
            preserve_default=False,
        ),
    ]