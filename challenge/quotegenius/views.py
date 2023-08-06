from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from serializers import UserSerializer, ProductSerializer, CustomerSerializer, PurchaseProductSerializer, PurchaseProductSerializer, SupplierProductSerializer, SupplierSerializer
from models import Customer, Product, Purchase, PurchaseProduct, Supplier, SupplierProduct

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseProductSerializer

class PurchaseProductViewSet(viewsets.ModelViewSet):
    queryset = PurchaseProduct.objects.all()
    serializer_class = PurchaseProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierProductViewSet(viewsets.ModelViewSet):
    queryset = SupplierProduct.objects.all()
    serializer_class = SupplierProductSerializer


