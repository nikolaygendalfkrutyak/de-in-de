# Generated by Django 5.1.5 on 2025-03-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
