# Generated by Django 4.2.1 on 2023-08-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
