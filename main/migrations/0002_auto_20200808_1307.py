# Generated by Django 3.0.6 on 2020-08-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
