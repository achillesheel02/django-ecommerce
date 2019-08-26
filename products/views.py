from django.views.generic import ListView, DetailView
from django.shortcuts import render


from .models import Product
# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
