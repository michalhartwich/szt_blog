from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200, blank=False, unique=True)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    visible_in_menu = models.BooleanField(default=True)
    show_title = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='./static/uploads')

    def __str__(self):
        return self.title

class Preferences(models.Model):
    homepage = models.ForeignKey(Page)
    site_name = models.CharField(max_length=200)
