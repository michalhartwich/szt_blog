# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_preferences_footer_column_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='homepage_image',
            field=models.CharField(default='https://blackrockdigital.github.io/startbootstrap-clean-blog/img/home-bg.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='preferences',
            name='homepage_subtitle',
            field=models.CharField(default='Page subtitle', max_length=200),
        ),
        migrations.AddField(
            model_name='preferences',
            name='homepage_title',
            field=models.CharField(default='Page title', max_length=200),
        ),
    ]
