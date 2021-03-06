# Generated by Django 3.1 on 2021-06-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20210603_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=1028, unique=True, verbose_name='slug'),
        ),
    ]
