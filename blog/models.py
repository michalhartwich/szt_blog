from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    image = models.ImageField(blank=True, upload_to='./static/uploads')

    def __str__(self):
        return self.title
