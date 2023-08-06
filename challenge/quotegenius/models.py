from django.db import models

class Product(models.Model):

    name = models.CharField(unique=True, null=False)
    barcode = models.CharField(unique=True, null=False)

class Customer(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)

class Supplier(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)
    email = models.CharField(unique=True, null=False, max_length=50)

class SupplierProduct(models.Model):

    supplier_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    quantity = models.DoubleField(null=Flase, default=1)
    price = models.DoubleField(null=False)

class Purchase(models.Model):

    supplier_id = models.IntegerField(null=False)
    customer_id = models.IntegerField(null=False)
    total_amount = models.DoubleField(null=False)

class PurchaseProduct(models.Model):

    product_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    quantity = models.DoubleField(null=False)
    price = models.DoubleField(null=False)