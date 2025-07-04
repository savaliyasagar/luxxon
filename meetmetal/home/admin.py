from django.contrib import admin
from home.models import *
# Register your models here.
 

class aboutadmin(admin.ModelAdmin):
    list_display = ('ourstory','storyimg','quality','qualityimg')
admin.site.register(aboutus,aboutadmin)
class SubProductDetailInline(admin.TabularInline):  # or admin.StackedInline
    model = SubProductDetail
    extra = 1  # Number of empty fields to display for adding more

# Customizing SubProduct Admin
class SubProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')  # Customize displayed columns
    prepopulated_fields = {"url_name": ("name",)}  # Auto-fill slug from name
    inlines = [SubProductDetailInline]  # Add Inline to allow multiple details

# Register models with custom admin
admin.site.register(Product)
admin.site.register(SubProduct, SubProductAdmin) 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    
# class Homeadmin(admin.ModelAdmin):
#     list_display = ('banner1','banner2','banner3','banner4')
admin.site.register(HomePage)



@admin.register(CatalogPage)
class CatalogPageAdmin(admin.ModelAdmin):
    list_display = ('page_number', 'front_image', 'back_image')
    
@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display = ('name','heading')
    
admin.site.register(copyrights)
admin.site.register(Testimonial)

admin.site.site_header = "Luxxon Hardware Admin"  # Change the admin header
admin.site.site_title = "Luxxon Hardware Portal"  # Change the title on the browser tab
admin.site.index_title = "Welcome to Luxxon Hardware Administration" 

@admin.register(ProductBanner)
class ProductBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if no banner exists
        return not ProductBanner.objects.exists()
    
@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow only one banner entry
        return not AboutBanner.objects.exists()
    
@admin.register(BlogBanner)
class BlogBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Restrict to one entry only
        return not BlogBanner.objects.exists()
    
admin.site.register(SiteConfiguration)