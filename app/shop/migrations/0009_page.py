# Generated by Django 5.0.5 on 2024-07-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0008_auto_20240705_0905"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("content", models.TextField()),
                ("is_head", models.BooleanField()),
                ("is_foot", models.BooleanField()),
                ("is_checkout", models.BooleanField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
