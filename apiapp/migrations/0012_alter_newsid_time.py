# Generated by Django 3.2 on 2022-08-25 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0011_auto_20220825_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 5, 15, 18, 917226)),
        ),
    ]
