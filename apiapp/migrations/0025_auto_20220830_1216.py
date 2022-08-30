# Generated by Django 3.2 on 2022-08-30 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0024_alter_newsid_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_id',
            field=models.BigIntegerField(blank=True, default=153636, null=True),
        ),
        migrations.AlterField(
            model_name='newsid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 30, 11, 16, 52, 636530)),
        ),
    ]
