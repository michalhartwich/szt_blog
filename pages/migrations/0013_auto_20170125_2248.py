# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_page_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='footer_column_count',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='homepage_image',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='homepage_subtitle',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='homepage_title',
        ),
    ]
