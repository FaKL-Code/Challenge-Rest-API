"""
URL configuration for challenge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from quotegenius.views import UserViewSet, CustomerViewSet, ProductViewSet, PurchaseViewSet, SupplierProductViewSet, SupplierViewSet, PurchaseProductViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/v1/customers', CustomerViewSet, basename='customer')
router.register(r'api/v1/products', ProductViewSet, basename='product')
router.register(r'api/v1/purchases', PurchaseViewSet, basename='purchase')
router.register(r'api/v1/purchaseproducts', PurchaseProductViewSet, basename='purchaseproduct')
router.register(r'api/v1/suppliers', SupplierViewSet, basename='supplier')
router.register(r'api/v1/supplierproducts', SupplierProductViewSet, basename='supplierproduct')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('auth.urls')),  
]
