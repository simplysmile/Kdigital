# Generated by Django 4.0.4 on 2022-06-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydata',
            name='day_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]