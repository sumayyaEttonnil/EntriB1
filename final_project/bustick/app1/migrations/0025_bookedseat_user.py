# Generated by Django 4.2.1 on 2023-11-27 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0024_bookedseat_bus_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookedseat",
            name="user",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
