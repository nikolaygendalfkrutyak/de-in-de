# Generated by Django 5.1.5 on 2025-03-08 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_footerinfo_opening_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerinfo',
            name='like_info',
        ),
    ]
