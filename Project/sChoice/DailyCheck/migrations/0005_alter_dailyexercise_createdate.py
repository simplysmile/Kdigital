# Generated by Django 4.0.4 on 2022-06-13 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyCheck', '0004_alter_dailyexercise_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyexercise',
            name='createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 14, 3, 51, 842652)),
        ),
    ]
