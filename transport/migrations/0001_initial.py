# Generated by Django 2.0.7 on 2018-08-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20)),
                ('route', models.CharField(max_length=30)),
                ('time_departure', models.TimeField()),
                ('time_return', models.TimeField()),
            ],
        ),
    ]
