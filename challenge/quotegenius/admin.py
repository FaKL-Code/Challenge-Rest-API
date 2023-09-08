from django.contrib import admin
from quotegenius.models import Product, Customer, Purchase, PurchaseProduct, Supplier, SupplierProduct

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
        fields = ['name',]

class ProductAdmin(admin.ModelAdmin):
        fields = ['name', 'barcode']

class PurchaseAdmin(admin.ModelAdmin):
        fields = ['supplier', 'customer', 'total_amount']

class PurchaseProductAdmin(admin.ModelAdmin):
        fields = ['product', 'purchase', 'quantity', 'price']

class SupplierAdmin(admin.ModelAdmin):
        fields = ['name', 'email']

class SupplierProductAdmin(admin.ModelAdmin):
        fields = ['supplier', 'product', 'quantity', 'price']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseProduct, PurchaseProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierProduct, SupplierProductAdmin)