# Generated by Django 3.1.6 on 2023-07-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='feature/')),
                ('icon', models.FileField(upload_to='feature/')),
                ('icon_background', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('testimonial_description', models.TextField()),
                ('testimonial_author', models.CharField(max_length=255)),
                ('author_designation', models.CharField(max_length=255)),
                ('testimonial_logo', models.FileField(upload_to='feature/')),
            ],
            options={
                'db_table': 'web_feature',
                'ordering': ['-id'],
            },
        ),
    ]
