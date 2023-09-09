from django.shortcuts import render

from rest_framework import filters

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from quotegenius.serializers import UserSerializer, ProductSerializer, CustomerSerializer, PurchaseProductSerializer, PurchaseSerializer, PurchaseProductSerializer, SupplierProductSerializer, SupplierSerializer
from quotegenius.models import Customer, Product, Purchase, PurchaseProduct, Supplier, SupplierProduct

from rest_framework.permissions import IsAuthenticated

from auditlog.mixins import LogAccessMixin
class UserViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = User.objects.none
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CustomerViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PurchaseViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['supplier__name', 'customer__name']

class PurchaseProductViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = PurchaseProduct.objects.all()
    serializer_class = PurchaseProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name', 'purchase__customer__name']

class SupplierViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class SupplierProductViewSet(LogAccessMixin, viewsets.ModelViewSet):
    queryset = SupplierProduct.objects.all()
    serializer_class = SupplierProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name']


