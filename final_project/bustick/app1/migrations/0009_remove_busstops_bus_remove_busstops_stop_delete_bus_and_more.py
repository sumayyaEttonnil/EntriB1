# Generated by Django 4.2.1 on 2023-11-14 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0008_rename_busstop_busstops_remove_bus_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="busstops",
            name="bus",
        ),
        migrations.RemoveField(
            model_name="busstops",
            name="stop",
        ),
        migrations.DeleteModel(
            name="Bus",
        ),
        migrations.DeleteModel(
            name="BusStops",
        ),
        migrations.DeleteModel(
            name="Stop",
        ),
    ]