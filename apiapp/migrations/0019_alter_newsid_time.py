# Generated by Django 3.2 on 2022-08-27 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0018_alter_newsid_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 22, 6, 22, 153049)),
        ),
    ]