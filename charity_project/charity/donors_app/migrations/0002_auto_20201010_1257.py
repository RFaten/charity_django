# Generated by Django 2.2 on 2020-10-10 10:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('donors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
