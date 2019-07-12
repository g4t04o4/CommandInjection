# Create your models here.
from django.db import models


class BlogPost(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    image = models.FilePathField()
    pub_date = models.DateTimeField()