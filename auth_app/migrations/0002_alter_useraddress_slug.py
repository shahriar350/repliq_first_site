# Generated by Django 4.1.5 on 2023-01-12 09:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='user_name', unique_with=('user__name',)),
        ),
    ]