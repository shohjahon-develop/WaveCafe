# Generated by Django 5.0 on 2024-08-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_about_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='index/img')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
    ]
