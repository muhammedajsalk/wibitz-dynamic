# Generated by Django 3.1.6 on 2023-07-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_videoblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('logo', models.FileField(upload_to='testimonial/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('author_designation', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'web_testimonial',
                'ordering': ['-id'],
            },
        ),
    ]