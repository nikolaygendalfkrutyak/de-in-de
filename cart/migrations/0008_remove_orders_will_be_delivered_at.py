# Generated by Django 5.1.5 on 2025-03-20 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_orders_accepted_orders_will_be_delivered_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='will_be_delivered_at',
        ),
    ]
