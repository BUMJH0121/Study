from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    
    kind = models.CharField('KIND', max_length=50, blank=False)
    title = models.CharField('TITLE', max_length=100)
    author = models.CharField('AUTHOR', max_length=50)
    display = models.CharField('DISPLAY', max_length=200)

    def __str__(self):
        return self.display
