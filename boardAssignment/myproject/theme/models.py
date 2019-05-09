from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField('date published')
    body = models.TextField()