# Generated by Django 2.0.7 on 2018-08-21 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_auto_20180820_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='Time_of_Transaction',
            field=models.TimeField(default=datetime.datetime(2018, 8, 21, 11, 22, 20, 861214, tzinfo=utc)),
        ),
    ]
