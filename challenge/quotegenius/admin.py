from django.contrib import admin
from quotegenius.models import Product, Customer, Purchase, PurchaseProduct, Supplier, SupplierProduct

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
        fields = ['name',]

class ProductAdmin(admin.ModelAdmin):
        fields = ['name', 'barcode']

class PurchaseAdmin(admin.ModelAdmin):
        fields = ['supplier_id', 'customer_id', 'total_amount']

class PurchaseProductAdmin(admin.ModelAdmin):
        fields = ['product_id', 'purchase_id', 'quantity', 'price']

class SupplierAdmin(admin.ModelAdmin):
        fields = ['name', 'email']

class SupplierProductAdmin(admin.ModelAdmin):
        fields = ['supplier_id', 'product_id', 'quantity', 'price']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseProduct, PurchaseProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierProduct, SupplierProductAdmin)