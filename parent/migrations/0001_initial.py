# Generated by Django 2.0.7 on 2018-08-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Father', models.CharField(max_length=64)),
                ('occupation_of_father', models.CharField(max_length=64)),
                ('Name_of_Mother', models.CharField(max_length=64)),
                ('occupation_of_mother', models.CharField(max_length=64)),
                ('Contact_No_Father', models.CharField(max_length=20)),
                ('Contact_No_Mother', models.CharField(max_length=20)),
                ('Address_Permanent', models.CharField(max_length=64)),
                ('Address_Current', models.CharField(max_length=64)),
                ('Related_Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
