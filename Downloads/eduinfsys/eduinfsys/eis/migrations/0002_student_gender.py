# Generated by Django 2.0.7 on 2018-07-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]