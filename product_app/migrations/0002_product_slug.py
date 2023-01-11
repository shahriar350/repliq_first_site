# Generated by Django 4.1.5 on 2023-01-11 09:09

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='hello-word', editable=False, populate_from='base_product__name', unique=True),
            preserve_default=False,
        ),
    ]
