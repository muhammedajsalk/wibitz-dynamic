# Generated by Django 3.1.6 on 2023-07-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_marketing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketing',
            name='image',
            field=models.FileField(upload_to='marketing/'),
        ),
    ]
