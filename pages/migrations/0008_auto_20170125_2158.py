# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
