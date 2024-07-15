# Generated by Django 5.0.2 on 2024-03-18 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funeral_services', '0007_remove_user_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='funeralbooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funeral_bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='legaldocument',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
