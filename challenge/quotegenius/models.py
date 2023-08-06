from django.db import models

class Product(models.Model):

    name = models.CharField(unique=True, null=False, max_length=255)
    barcode = models.CharField(unique=True, null=False, max_length=255)

class Customer(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)

class Supplier(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)
    email = models.CharField(unique=True, null=False, max_length=50)

class SupplierProduct(models.Model):

    supplier_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    quantity = models.FloatField(null=False, default=1)
    price = models.FloatField(null=False)

class Purchase(models.Model):

    supplier_id = models.IntegerField(null=False)
    customer_id = models.IntegerField(null=False)
    total_amount = models.FloatField(null=False)

class PurchaseProduct(models.Model):

    product_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    quantity = models.FloatField(null=False)
    price = models.FloatField(null=False)