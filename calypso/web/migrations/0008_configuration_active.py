# Generated by Django 3.1 on 2020-12-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_configuration_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
