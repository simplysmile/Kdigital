# Generated by Django 4.0.4 on 2022-06-13 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 13, 59, 40, 75597)),
        ),
        migrations.AlterField(
            model_name='members',
            name='modidate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 13, 59, 40, 75597)),
        ),
    ]