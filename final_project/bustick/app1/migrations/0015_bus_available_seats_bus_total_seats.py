# Generated by Django 4.2.1 on 2023-11-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0014_boardingstop_destinationstop_remove_bus_stops_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bus",
            name="available_seats",
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name="bus",
            name="total_seats",
            field=models.IntegerField(default=50),
        ),
    ]