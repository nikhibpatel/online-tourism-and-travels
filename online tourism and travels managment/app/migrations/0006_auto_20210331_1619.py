# Generated by Django 3.1.6 on 2021-03-31 10:49

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None),
        ),
    ]
