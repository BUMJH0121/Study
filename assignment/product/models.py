from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    stock_quqnity = models.CharField(max_length=100)
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name