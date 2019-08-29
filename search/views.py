from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.
class SearchProductView(ListView):
    template_name = 'search/search_list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        else:
            return Product.objects.none()