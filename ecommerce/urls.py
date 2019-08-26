"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import LoginPage,RegisterPage,HomePage
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductListView, ProductDetailView, ProductFeaturedView


urlpatterns = [
    url(r'^$', HomePage),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginPage),
    url(r'^register/$', RegisterPage),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/featured/$', ProductFeaturedView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailView.as_view()),

]

if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
