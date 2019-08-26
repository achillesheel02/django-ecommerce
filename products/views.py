from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404


from .models import Product
# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = Product.objects.get(slug=slug)
        return instance

class ProductFeaturedView(ListView):
    template_name = 'products/products-featured.html'

    def get_queryset(self):
        return Product.objects.filter(featured=True)