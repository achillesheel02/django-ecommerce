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

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title