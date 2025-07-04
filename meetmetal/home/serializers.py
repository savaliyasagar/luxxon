# home/serializers.py

from rest_framework import serializers
from .models import (
    HomePage, aboutus, AboutBanner, Product, ProductBanner, SubProduct,
    SubProductDetail, Contact, CatalogPage, Blog, copyrights, Testimonial,
    BlogBanner, SiteConfiguration
)

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutus
        fields = '__all__'

class AboutBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutBanner
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBanner
        fields = '__all__'

class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProduct
        fields = '__all__'

class SubProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProductDetail
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CatalogPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogPage
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CopyrightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = copyrights
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class BlogBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogBanner
        fields = '__all__'

class SiteConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'