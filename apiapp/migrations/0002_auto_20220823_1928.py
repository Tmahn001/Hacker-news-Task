# Generated by Django 3.2 on 2022-08-23 19:28

import apiapp.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=apiapp.models.UCDateTimeField(),
        ),
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 19, 28, 24, 479311)),
        ),
    ]
