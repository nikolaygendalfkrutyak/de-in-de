# Generated by Django 5.1.5 on 2025-03-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detailed_description',
            field=models.TextField(default=''),
        ),
    ]
