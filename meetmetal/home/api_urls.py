# api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    HomePageViewSet, AboutUsViewSet, AboutBannerViewSet, ProductViewSet,
    ProductBannerViewSet, SubProductViewSet, SubProductDetailViewSet,
    ContactViewSet, CatalogPageViewSet, BlogViewSet, CopyrightsViewSet,
    TestimonialViewSet, BlogBannerViewSet, SiteConfigurationViewSet
)

router = DefaultRouter()
router.register(r'homepage', HomePageViewSet)
router.register(r'aboutus', AboutUsViewSet)
router.register(r'aboutbanner', AboutBannerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productbanner', ProductBannerViewSet)
router.register(r'subproducts', SubProductViewSet)
router.register(r'subproductdetails', SubProductDetailViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'catalogpages', CatalogPageViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'copyrights', CopyrightsViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'blogbanner', BlogBannerViewSet)
router.register(r'siteconfiguration', SiteConfigurationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]