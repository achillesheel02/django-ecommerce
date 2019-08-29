from django.db import models
import os
import random
from datetime import datetime
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

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

    def get_by_slug(self,slug):
        qs = self.get_queryset().filter(slug=slug)
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
    slug = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)