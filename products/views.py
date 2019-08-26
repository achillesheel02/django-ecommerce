from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404


from .models import Product
# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist.")
        return instance