# Generated by Django 2.2.3 on 2019-07-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20190714_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=None, upload_to='Book/media'),
            preserve_default=False,
        ),
    ]
