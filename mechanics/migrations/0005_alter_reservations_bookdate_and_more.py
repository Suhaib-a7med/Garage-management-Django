# Generated by Django 5.0 on 2024-03-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mechanics", "0004_reservations_booktime_reservations_mechanic_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservations",
            name="bookDate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="reservations",
            name="bookTime",
            field=models.TimeField(),
        ),
    ]
