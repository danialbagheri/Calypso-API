# Generated by Django 3.1 on 2021-02-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20201215_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='opened',
            field=models.BooleanField(default=False),
        ),
    ]
