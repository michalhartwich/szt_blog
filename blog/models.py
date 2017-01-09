from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField('body')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
