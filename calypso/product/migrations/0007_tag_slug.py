# Generated by Django 3.1 on 2021-04-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210412_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, default=154, verbose_name='slug'),
        ),
    ]
