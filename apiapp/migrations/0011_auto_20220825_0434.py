# Generated by Django 3.2 on 2022-08-25 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0010_alter_newsid_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 4, 34, 50, 512874)),
        ),
    ]
