"""
URL configuration for meetmetal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path("products/", views.products_view, name="products"),
    path("products/<slug:product_slug>/", views.subproducts_view, name="subproducts"),
    path("products/<slug:product_slug>/<slug:subproduct_slug>/", views.subproduct_details_view, name="subproduct_details"),
    path("contact/", views.contact, name="contact"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("blog/", views.blog, name="blog"),
    path('api/', include('home.api_urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 