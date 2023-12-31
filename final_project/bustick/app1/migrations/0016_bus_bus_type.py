# Generated by Django 4.2.1 on 2023-11-15 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0015_bus_available_seats_bus_total_seats"),
    ]

    operations = [
        migrations.AddField(
            model_name="bus",
            name="bus_type",
            field=models.CharField(
                choices=[
                    ("AC-Sleeper", "AC Sleeper"),
                    ("Non-AC-Sleeper", "Non-AC Sleeper"),
                    ("AC-Non-Sleeper", "AC Non-Sleeper"),
                    ("Non-AC-Non-Sleeper", "Non-AC Non-Sleeper"),
                ],
                default="Non-AC-Non-Sleeper",
                max_length=30,
            ),
        ),
    ]
