# Generated by Django 3.1.6 on 2021-05-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='images',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
