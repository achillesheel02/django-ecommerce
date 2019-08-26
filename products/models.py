from django.db import models
import os
import random
from datetime import datetime

# Create your models here.


def upload_image_path(instance, filename):
    now = datetime.now()  #
    randint=random.randint(1,99999999)
    name, ext = os.path.splitext(os.path.basename(filename))
    return "products/{year}/{month}/{day}/{randint}{ext}".format(randint=randint, ext=ext, year=now.strftime("%Y"), month=now.strftime("%m"),\
                                                                 day=now.strftime("%d"))


class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs
        return None

    def featured(self):
        qs = self.get_queryset().filter(featured=True)
        if qs.count() == 1:
            return qs
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title