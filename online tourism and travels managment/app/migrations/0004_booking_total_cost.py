# Generated by Django 3.1.6 on 2021-03-31 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210318_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
    ]
