# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20170125_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='/static/uploads'),
        ),
    ]
