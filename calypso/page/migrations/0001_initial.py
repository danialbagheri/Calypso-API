# Generated by Django 3.1 on 2020-12-18 09:47

from django.db import migrations, models
import django_grapesjs.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('html', django_grapesjs.models.fields.GrapesJsHtmlField()),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
    ]
