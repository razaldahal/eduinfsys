# Generated by Django 2.0.7 on 2018-08-28 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0013_auto_20180827_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='Time_of_Transaction',
            field=models.TimeField(default=datetime.datetime(2018, 8, 28, 7, 59, 45, 823111, tzinfo=utc)),
        ),
    ]