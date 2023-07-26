# Generated by Django 3.1.6 on 2023-07-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_customer_white_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='product',
            name='hero_image',
            field=models.ImageField(default='a', upload_to='product/hero_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='studio', max_length=255),
            preserve_default=False,
        ),
    ]