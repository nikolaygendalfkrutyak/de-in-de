# Generated by Django 5.1.5 on 2025-02-15 10:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_chosenproduct_cart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=75)),
                ('opening_hours', ckeditor.fields.RichTextField()),
                ('like_info', ckeditor.fields.RichTextField()),
                ('like_info_more', models.TextField()),
                ('about_us', models.TextField()),
                ('contact_us', models.TextField()),
                ('privacy_policy', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('return_policy', models.TextField()),
                ('faqs_and_help', models.TextField()),
                ('account', models.TextField()),
                ('shop_details', models.TextField()),
                ('shopping_cart', models.TextField()),
                ('wishlist', models.TextField()),
                ('order_history', models.TextField()),
                ('international_order', models.TextField()),
            ],
        ),
    ]
