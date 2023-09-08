from django.db import models

class Product(models.Model):

    name = models.CharField(unique=True, null=False, max_length=255)
    barcode = models.CharField(unique=True, null=False, max_length=255)

    def __set__(self):
        return "{} - {}".format(self.name, self.barcode)

class Customer(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)

    def __set__(self):
        return "{} - {}".format(self.name)

class Supplier(models.Model):

    name = models.CharField(unique=True, null=False, max_length=50)
    email = models.CharField(unique=True, null=False, max_length=50)

    def __set__(self):
        return "{} - {}".format(self.name, self.email)

class SupplierProduct(models.Model):

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier_id")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_id")
    quantity = models.FloatField(null=False, default=1)
    price = models.FloatField(null=False)

    def __set__(self):
        return "{} - {}".format(self.supplier, self.product, self.quantity, self.price)

class Purchase(models.Model):

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier_id_purchase")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_id_purchase")
    total_amount = models.FloatField(null=False)

    def __set__(self):
        return "{} - {}".format(self.supplier, self.customer, self.total_amount)

class PurchaseProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_id_purchase")
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="purchase_id_purchase")
    quantity = models.FloatField(null=False)
    price = models.FloatField(null=False)

    def __set__(self):
        return "{} - {}".format(self.product, self.purchase, self.quantity, self.price)