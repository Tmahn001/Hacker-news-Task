# Generated by Django 3.2 on 2022-08-23 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_auto_20220823_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 23, 12, 31, 840377)),
        ),
    ]