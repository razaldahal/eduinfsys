# Generated by Django 2.0.7 on 2018-08-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
    ]