# Generated by Django 3.1 on 2021-05-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210505_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=9784, unique=True, verbose_name='slug'),
        ),
    ]
