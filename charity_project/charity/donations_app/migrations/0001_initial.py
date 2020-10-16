# Generated by Django 2.2 on 2020-10-10 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donors_app', '0002_auto_20201010_1257'),
        ('cases_app', '0003_auto_20201010_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.PositiveIntegerField()),
                ('paid_flag', models.BooleanField()),
                ('case_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cases_app.Cases')),
                ('donor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donors_app.Donors')),
            ],
        ),
    ]
