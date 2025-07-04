from django.db import models,migrations
from django.urls import reverse
from django.utils import timezone
# Create your models here.
 
class HomePage(models.Model):
    banner1 = models.ImageField(upload_to='home/')
    banner2 = models.ImageField(upload_to='home/')
    banner3 = models.ImageField(upload_to='home/')
    banner4 = models.ImageField(upload_to='home/')
    welcome_image = models.ImageField(upload_to='home/')
    welcome_description = models.TextField()
    gallery1 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery2 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery3 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery4 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery5 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery6 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery7 = models.ImageField(upload_to='home/', default='default_image.jpg')
    gallery8 = models.ImageField(upload_to='home/', default='default_image.jpg')
class aboutus(models.Model):
    ourstory = models.TextField()
    storyimg = models.ImageField(upload_to='about/')
    quality = models.TextField()
    qualityimg = models.ImageField(upload_to='about/')
class AboutBanner(models.Model):
    banner_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return "About Page Banner"

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    homeproductimage = models.ImageField(upload_to="products/")
    url_name = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("subproducts", kwargs={"product_slug": self.url_name})

    def __str__(self):
        return self.name
    
class ProductBanner(models.Model):
    banner_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return "Product Banner"


class SubProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="subproducts")
    name = models.CharField(max_length=255)
    before_image = models.ImageField(upload_to="subproducts/")
    after_image = models.ImageField(upload_to="subproducts/")
    url_name = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("subproduct_details", kwargs={
            "product_slug": self.product.url_name,
            "subproduct_slug": self.url_name
        })

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class SubProductDetail(models.Model):
    subproduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE, related_name="details")
    product_code = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subproduct.name} - {self.product_code}"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.submitted_at}"
    
class CatalogPage(models.Model):
    page_number = models.IntegerField(unique=True)
    front_image = models.ImageField(upload_to='catalog_images/')
    back_image = models.ImageField(upload_to='catalog_images/')

    def __str__(self):
        return f"Page {self.page_number}"
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    Blog_image = models.ImageField(upload_to='blog/')
    heading = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class copyrights(models.Model):
    Copyrights = models.TextField()
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField()
    
    def __str__(self):
        return self.name
class BlogBanner(models.Model):
    banner_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return "Blog Page Banner"
class SiteConfiguration(models.Model):
    instagram = models.URLField(default='https://www.instagram.com/', blank=True)
    linkedin = models.URLField(default='https://www.linkedin.com/', blank=True)
    facebook = models.URLField(default='https://www.facebook.com/', blank=True)

    def __str__(self):
        return "Site Configuration"