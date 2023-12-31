# Generated by Django 4.2.4 on 2023-09-08 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotegenius', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='supplier_id',
        ),
        migrations.RemoveField(
            model_name='purchaseproduct',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='purchaseproduct',
            name='purchase_id',
        ),
        migrations.RemoveField(
            model_name='supplierproduct',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='supplierproduct',
            name='supplier_id',
        ),
        migrations.AddField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_id_purchase', to='quotegenius.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_id_purchase', to='quotegenius.supplier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_purchase', to='quotegenius.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseproduct',
            name='purchase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_id_purchase', to='quotegenius.purchase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplierproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_supplier', to='quotegenius.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplierproduct',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_id_supplier', to='quotegenius.supplier'),
            preserve_default=False,
        ),
    ]
