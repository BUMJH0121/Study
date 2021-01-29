from django.db import models
from django.urls import reverse
# Create your models here.
class Weather(models.Model):
    
    city = models.CharField('CITY', max_length=100, blank=False)
    temperature = models.CharField('TEMPERATURE', max_length=100)
    skt = models.CharField('SKY', max_length=100)

    def __str__(self):
        return self.city
