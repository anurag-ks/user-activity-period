# Generated by Django 3.0.6 on 2020-08-08 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=200, verbose_name='Real Name')),
                ('time_zone', models.CharField(max_length=200, verbose_name='Time Zone')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UserModel', verbose_name='user')),
            ],
        ),
    ]
