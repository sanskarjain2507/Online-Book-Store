# Generated by Django 2.2.3 on 2019-07-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20190717_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
