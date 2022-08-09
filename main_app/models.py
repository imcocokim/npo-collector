from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
class NPO(models.Model):
  name = models.CharField(max_length=100)
  topic = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  website = models.URLField
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name