# Generated by Django 4.2.1 on 2023-07-25 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_product_items_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.product"
                    ),
                ),
            ],
        ),
    ]
