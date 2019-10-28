# Generated by Django 2.2.3 on 2019-07-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default=None, max_length=30)),
                ('middleName', models.CharField(default=None, max_length=30)),
                ('lastName', models.CharField(default=None, max_length=30)),
                ('mobileNo', models.IntegerField(default=None)),
                ('empName', models.CharField(default=None, max_length=30)),
                ('password', models.CharField(default=None, max_length=500)),
                ('emailAdd', models.EmailField(default=None, max_length=40)),
                ('salary', models.IntegerField(default=None)),
                ('experience', models.IntegerField(default=None)),
                ('age', models.IntegerField(default=None)),
                ('temporaryAddress', models.TextField(default=None, max_length=300)),
                ('tPincode', models.IntegerField(default=None)),
                ('permanentAddress', models.TextField(default=None, max_length=300)),
                ('pPincode', models.IntegerField(default=None)),
            ],
            options={
                'db_table': 'Employee_Information',
            },
        ),
    ]