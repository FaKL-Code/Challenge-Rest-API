from rest_framework import serializers

from django.contrib.auth.models import User
from quotegenius.models import Customer, Product, Purchase, PurchaseProduct, Supplier, SupplierProduct

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name',)
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name', 'email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'barcode')

class PurchaseSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Purchase
        fields = ('supplier', 'customer', 'total_amount')

class PurchaseProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    purchase = PurchaseSerializer()
    class Meta:
        model = PurchaseProduct
        fields = ('product', 'purchase', 'quantity', 'price')

class SupplierProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    product = ProductSerializer()
    class Meta:
        model = SupplierProduct
        fields = ('supplier', 'product', 'quantity', 'price')