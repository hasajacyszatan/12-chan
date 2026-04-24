from django.db import models

# Create your models here.
from django.db import models
class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)