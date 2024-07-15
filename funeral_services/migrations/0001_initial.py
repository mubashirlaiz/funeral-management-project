# Generated by Django 5.0.2 on 2024-02-29 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caste', models.CharField(max_length=50)),
                ('current_location', models.CharField(max_length=200)),
                ('funeral_location', models.CharField(max_length=200)),
                ('has_relatives', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LegalDocumentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funeral_services.user')),
            ],
        ),
        migrations.CreateModel(
            name='FuneralBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('booking_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funeral_services.user')),
            ],
        ),
    ]
