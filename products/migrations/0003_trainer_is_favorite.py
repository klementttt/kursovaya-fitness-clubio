# Generated by Django 5.0.4 on 2024-06-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_booking_cart_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
