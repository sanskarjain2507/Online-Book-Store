# Generated by Django 2.2.3 on 2019-09-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_auto_20190907_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='middleName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]