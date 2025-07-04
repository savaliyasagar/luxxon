# views.py
from django.shortcuts import render, redirect, get_object_or_404
from home.models import *
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    HomePageSerializer, AboutUsSerializer, AboutBannerSerializer,
    ProductSerializer, ProductBannerSerializer, SubProductSerializer,
    SubProductDetailSerializer, ContactSerializer, CatalogPageSerializer,
    BlogSerializer, CopyrightsSerializer, TestimonialSerializer,
    BlogBannerSerializer, SiteConfigurationSerializer
)

# Regular views remain unchanged
def home(request):
    home_data = HomePage.objects.first()
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    Testimonial_data = Testimonial.objects.all()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'home_data':home_data,
        'product_data':products,
        'copyrights_data':copyrights_data,
        'Testimonial_data':Testimonial_data,
        'social_links': social_links,
    }
    return render(request, 'index.html',context)

def about(request):
    about_data = aboutus.objects.first()
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    about_banner = AboutBanner.objects.first()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'about_data':about_data,
        'product_data':products,
        'copyrights_data':copyrights_data,
        'about_banner':about_banner,
        'social_links':social_links,
    }
    return render(request, 'about.html',context)

def products_view(request):
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    product_banner = ProductBanner.objects.first()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'product_data':products,
        'copyrights_data':copyrights_data,
        'social_links':social_links,
        'product_banner':product_banner,
    }
    return render(request, "products.html", context)

def subproducts_view(request, product_slug):
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    product = get_object_or_404(Product, url_name=product_slug)
    subproducts = product.subproducts.all()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'product_data':products,
        'copyrights_data':copyrights_data,
        'social_links':social_links,
        "product": product,
        "subproducts": subproducts,
    }
    return render(request, "subproducts.html", context)

def subproduct_details_view(request, product_slug, subproduct_slug):
    product = get_object_or_404(Product, url_name=product_slug)
    copyrights_data = copyrights.objects.all()
    products = Product.objects.all()
    subproduct = get_object_or_404(SubProduct, url_name=subproduct_slug, product=product)
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'product_data':products,
        'copyrights_data':copyrights_data,
        'social_links':social_links,
        "product": product,
        "subproduct": subproduct,
    }
    return render(request, "subproduct_details.html", context)

def contact(request):
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'product_data': products,
        'copyrights_data':copyrights_data,
        'social_links':social_links
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html', context)

def catalogue(request):
    products = Product.objects.all()
    copyrights_data = copyrights.objects.all()
    catalog_pages = CatalogPage.objects.order_by('page_number')
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'catalog_pages': catalog_pages,
        'product_data': products,
        'copyrights_data':copyrights_data,
        'social_links':social_links
    }
    return render(request, 'catalogue.html', context)

def blog(request):
    blog_data = Blog.objects.all()
    copyrights_data = copyrights.objects.all()
    products = Product.objects.all()
    blog_banner = BlogBanner.objects.first()
    site_config = SiteConfiguration.objects.first()
    social_links = {
        'instagram': site_config.instagram if site_config else '#',
        'linkedin': site_config.linkedin if site_config else '#',
        'facebook': site_config.facebook if site_config else '#',
    }

    context = {
        'blog_data':blog_data, 
        'product_data': products,
        'copyrights_data':copyrights_data, 
        "blog_banner": blog_banner,
        "social_links":social_links
    }
    return render(request, 'blog.html', context)

# API ViewSets with Authentication
class HomePageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [IsAuthenticated]

class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = aboutus.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAuthenticated]

class AboutBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutBanner.objects.all()
    serializer_class = AboutBannerSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductBanner.objects.all()
    serializer_class = ProductBannerSerializer
    permission_classes = [IsAuthenticated]

class SubProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubProduct.objects.all()
    serializer_class = SubProductSerializer
    permission_classes = [IsAuthenticated]

class SubProductDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubProductDetail.objects.all()
    serializer_class = SubProductDetailSerializer
    permission_classes = [IsAuthenticated]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class CatalogPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatalogPage.objects.all()
    serializer_class = CatalogPageSerializer
    permission_classes = [IsAuthenticated]

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

class CopyrightsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = copyrights.objects.all()
    serializer_class = CopyrightsSerializer
    permission_classes = [IsAuthenticated]

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticated]

class BlogBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogBanner.objects.all()
    serializer_class = BlogBannerSerializer
    permission_classes = [IsAuthenticated]

class SiteConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationSerializer
    permission_classes = [IsAuthenticated]