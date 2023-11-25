# Generated by Django 4.2.1 on 2023-11-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0019_boardingstop_distance_destinationstop_distance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bus",
            name="bus_type",
            field=models.CharField(
                choices=[
                    ("AC-Sleeper", "AC-Sleeper"),
                    ("Non-AC-Sleeper", "Non-AC-Sleeper"),
                    ("AC-seater", "AC-seater"),
                    ("Non-AC-seater", "Non-AC-seater"),
                ],
                default="Non-AC-Non-Sleeper",
                max_length=30,
            ),
        ),
    ]