# Generated by Django 3.2.2 on 2022-11-17 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('meta_keywords', models.CharField(max_length=200)),
                ('meta_description', models.TextField(max_length=160)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('header', models.CharField(blank=True, max_length=50, null=True)),
                ('google_analytics', models.TextField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]