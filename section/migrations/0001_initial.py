# Generated by Django 2.0.7 on 2018-08-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=2)),
                ('r_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classe.classe')),
            ],
        ),
    ]
