# Generated by Django 3.1 on 2020-10-09 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='option_name',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='option_value',
        ),
    ]
