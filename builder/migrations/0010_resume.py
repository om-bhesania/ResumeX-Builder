# Generated by Django 4.2.1 on 2023-06-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0009_remove_uploadedfile_files_delete_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('html_content', models.TextField()),
            ],
        ),
    ]
