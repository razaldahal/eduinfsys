# Generated by Django 2.0.7 on 2018-08-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=11)),
                ('Section', models.CharField(max_length=2)),
                ('roll_no', models.IntegerField()),
                ('Name', models.CharField(max_length=64)),
                ('Father_name', models.CharField(max_length=64)),
                ('Mother_name', models.CharField(max_length=64)),
                ('Guardians_name', models.CharField(max_length=64)),
                ('Guardians_contact', models.CharField(max_length=64)),
                ('Address_Current', models.CharField(max_length=64)),
                ('Address_Permanent', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
            ],
        ),
    ]