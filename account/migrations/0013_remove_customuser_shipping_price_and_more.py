# Generated by Django 5.1.5 on 2025-03-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_customuser_shipping_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='shipping_price',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subtotal',
        ),
    ]
