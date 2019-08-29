from django.conf.urls import url
from .views import ProductListView, ProductDetailView, ProductFeaturedView

app_name='products'

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^featured/$', ProductFeaturedView.as_view(),name='featured'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail'),

]
