# Generated by Django 5.1.5 on 2025-02-14 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['sort'], 'verbose_name_plural': 'Carts'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='change_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='sort',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ChosenProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_products', to='main.cart')),
            ],
            bases=('main.product',),
        ),
    ]
