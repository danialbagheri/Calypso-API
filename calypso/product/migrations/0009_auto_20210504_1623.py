# Generated by Django 3.1 on 2021-05-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210413_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=9474, unique=True, verbose_name='slug'),
        ),
    ]
