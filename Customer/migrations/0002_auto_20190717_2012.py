# Generated by Django 2.2.3 on 2019-07-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default=None, max_length=300),
        ),
    ]