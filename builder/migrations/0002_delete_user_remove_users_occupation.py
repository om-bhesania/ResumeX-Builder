# Generated by Django 4.2.1 on 2023-06-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='users',
            name='occupation',
        ),
    ]
