# Generated by Django 4.1.2 on 2022-10-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='nacimiento',
            field=models.CharField(max_length=20),
        ),
    ]