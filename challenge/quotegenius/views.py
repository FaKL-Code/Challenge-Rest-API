from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from quotegenius.serializers import UserSerializer, ProductSerializer, CustomerSerializer, PurchaseProductSerializer, PurchaseSerializer, PurchaseProductSerializer, SupplierProductSerializer, SupplierSerializer
from quotegenius.models import Customer, Product, Purchase, PurchaseProduct, Supplier, SupplierProduct

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['supplier_id', 'customer_id']

class PurchaseProductViewSet(viewsets.ModelViewSet):
    queryset = PurchaseProduct.objects.all()
    serializer_class = PurchaseProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['product_id', 'purchase_id']

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']

class SupplierProductViewSet(viewsets.ModelViewSet):
    queryset = SupplierProduct.objects.all()
    serializer_class = SupplierProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['product_id', 'supplier_id']


