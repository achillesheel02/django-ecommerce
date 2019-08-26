from django.conf.urls import url
from .views import ProductListView, ProductDetailView, ProductFeaturedView


urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^featured/$', ProductFeaturedView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view()),

]
