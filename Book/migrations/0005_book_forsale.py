# Generated by Django 2.2.3 on 2019-07-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20190715_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='forSale',
            field=models.CharField(default='yes', max_length=10),
            preserve_default=False,
        ),
    ]
