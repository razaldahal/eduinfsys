# Generated by Django 2.0.7 on 2018-08-06 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20180806_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='Time_of_Transaction',
            field=models.TimeField(default=datetime.datetime(2018, 8, 6, 20, 14, 51, 564907, tzinfo=utc)),
        ),
    ]