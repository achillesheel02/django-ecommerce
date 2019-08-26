from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(mx_length=120)
    description = models.TextField()
