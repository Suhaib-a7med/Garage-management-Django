# Generated by Django 5.0 on 2024-03-20 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mechanics", "0002_remove_mechanics_years_alter_mechanics_mobile_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mechanics",
            options={"managed": True},
        ),
        migrations.AlterModelOptions(
            name="reservations",
            options={"managed": True},
        ),
        migrations.AlterModelTable(
            name="mechanics",
            table="mechanics",
        ),
        migrations.AlterModelTable(
            name="reservations",
            table="reservation",
        ),
    ]
