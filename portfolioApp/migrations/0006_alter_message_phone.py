# Generated by Django 3.2.2 on 2022-04-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0005_auto_20220407_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
