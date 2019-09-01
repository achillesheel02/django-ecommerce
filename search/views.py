from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
class SearchProductView(ListView):
    template_name = 'search/search_list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(lookups).distinct()
        else:
            return Product.objects.none()