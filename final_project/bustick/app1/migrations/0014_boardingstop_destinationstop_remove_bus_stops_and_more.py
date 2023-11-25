# Generated by Django 4.2.1 on 2023-11-14 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0013_busstoproute_departure_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardingStop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("departure_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="DestinationStop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("arrival_time", models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name="bus",
            name="stops",
        ),
        migrations.DeleteModel(
            name="BusStopRoute",
        ),
        migrations.AddField(
            model_name="destinationstop",
            name="bus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.bus"
            ),
        ),
        migrations.AddField(
            model_name="destinationstop",
            name="stop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.stop"
            ),
        ),
        migrations.AddField(
            model_name="boardingstop",
            name="bus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.bus"
            ),
        ),
        migrations.AddField(
            model_name="boardingstop",
            name="stop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.stop"
            ),
        ),
        migrations.AddField(
            model_name="bus",
            name="boarding_stops",
            field=models.ManyToManyField(
                related_name="boarding_buses",
                through="app1.BoardingStop",
                to="app1.stop",
            ),
        ),
        migrations.AddField(
            model_name="bus",
            name="destination_stops",
            field=models.ManyToManyField(
                related_name="destination_buses",
                through="app1.DestinationStop",
                to="app1.stop",
            ),
        ),
    ]