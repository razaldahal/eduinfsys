# Generated by Django 2.0.7 on 2018-08-19 08:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20180819_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='Time_of_Transaction',
            field=models.TimeField(default=datetime.datetime(2018, 8, 19, 8, 51, 40, 206014, tzinfo=utc)),
        ),
    ]
