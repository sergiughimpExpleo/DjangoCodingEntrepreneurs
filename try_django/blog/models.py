from django.db import models
from django.db.models.fields import TextField

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
