# Generated by Django 5.1.5 on 2025-03-19 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_testimonial_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='main.product'),
        ),
    ]
