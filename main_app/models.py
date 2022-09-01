from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

TOPICS = (
  ('AN', 'Animal Protection & Welfare'),
  ('EV', 'Environment'),
  ('ED', 'Education'),
  ('H', 'Health'),
  ('HC', 'Human & Civil Rights'),
  ('HS', 'Human Services'),
  ('I', 'International Relief')
)

# Create your models here.
class NPO(models.Model):
  name = models.CharField(max_length=100)
  topic = models.CharField(
    max_length=100,
    choices=TOPICS,
    default=TOPICS[0][0]
    )
  description = models.TextField(max_length=1000)
  website = models.URLField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} represents {self.get_topic_display()}'
  
  def get_absolute_url(self):
      return reverse('npos_detail', kwargs={'npo_id': self.id})

class Event(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=100)
  npo = models.ForeignKey(NPO, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.title} on {self.date}'

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  npo = models.OneToOneField(NPO, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for npo_id: {self.npo_id} @{self.url}"