from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    image = models.URLField()
    price = models.FloatField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )