# Generated by Django 5.1.5 on 2025-03-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_testimonial_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='is_appropriate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
