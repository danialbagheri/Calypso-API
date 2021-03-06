# Generated by Django 3.1 on 2021-01-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201208_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='keyword',
            field=models.ManyToManyField(blank=True, to='product.Keyword', verbose_name='keywords'),
        ),
    ]
