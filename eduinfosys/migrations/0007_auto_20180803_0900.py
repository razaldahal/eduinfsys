# Generated by Django 2.0.7 on 2018-08-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduinfosys', '0006_accounting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='Date_of_Transaction',
            field=models.DateField(),
        ),
    ]
