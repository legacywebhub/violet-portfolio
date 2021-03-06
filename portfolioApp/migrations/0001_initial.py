# Generated by Django 3.2.2 on 2022-04-20 10:22

import ckeditor.fields
import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/contents')),
                ('content', ckeditor.fields.RichTextField(max_length=20000)),
                ('quote', models.CharField(blank=True, max_length=250, null=True)),
                ('ad', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('location', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=30)),
                ('my_image', models.ImageField(blank=True, upload_to='images/about')),
                ('about_me', models.TextField(max_length=500)),
                ('about_services', models.TextField(blank=True, max_length=2000)),
                ('about_team', models.TextField(blank=True, max_length=1000)),
                ('CV', models.FileField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='documents')),
                ('address', models.CharField(max_length=150)),
                ('email_1', models.EmailField(max_length=254)),
                ('email_2', models.EmailField(blank=True, max_length=254)),
                ('phone_1', models.CharField(max_length=20)),
                ('phone_2', models.CharField(blank=True, max_length=20)),
                ('phone_3', models.CharField(blank=True, max_length=20)),
                ('whatsapp', models.URLField(blank=True, max_length=300)),
                ('facebook', models.URLField(blank=True, max_length=300)),
                ('twitter', models.URLField(blank=True, max_length=300)),
                ('instagram', models.URLField(blank=True, max_length=300)),
                ('tiktok', models.URLField(blank=True, max_length=300)),
                ('linked_in', models.URLField(blank=True, max_length=300)),
                ('youtube', models.URLField(blank=True, max_length=300)),
                ('pin_interest', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=10000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(choices=[('category-a', 'category-a'), ('category-b', 'category-b'), ('category-c', 'category-c'), ('category-d', 'category-d')], default='category-a', max_length=25)),
                ('service', models.CharField(max_length=25)),
                ('author', models.CharField(blank=True, max_length=25)),
                ('image', models.ImageField(upload_to='images/portfolio')),
                ('detail', models.TextField(blank=True, max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('detail', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/team')),
                ('role', models.CharField(max_length=50)),
                ('skill1', models.CharField(blank=True, max_length=25)),
                ('skill2', models.CharField(blank=True, max_length=25)),
                ('skill3', models.CharField(blank=True, max_length=25)),
                ('whatsapp', models.URLField(blank=True, max_length=300)),
                ('facebook', models.URLField(blank=True, max_length=300)),
                ('twitter', models.URLField(blank=True, max_length=300)),
                ('instagram', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_image', models.ImageField(upload_to='images/testimonials')),
                ('service', models.CharField(max_length=50)),
                ('testimony', models.CharField(max_length=3000)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('meta_keywords', models.CharField(max_length=200)),
                ('meta_description', models.TextField(max_length=160)),
                ('logo', models.ImageField(blank=True, upload_to='images/setting')),
                ('header', models.CharField(blank=True, max_length=50, null=True)),
                ('google_analytics', models.TextField(blank=True, max_length=1500)),
            ],
        ),
    ]
