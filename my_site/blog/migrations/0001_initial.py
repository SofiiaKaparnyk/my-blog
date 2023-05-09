# Generated by Django 4.2.1 on 2023-05-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("date", models.TimeField(auto_now_add=True)),
                ("slug", models.SlugField(unique=True)),
                ("img", models.CharField()),
                ("author", models.CharField()),
                ("title", models.CharField()),
                ("excerpt", models.CharField()),
                ("content", models.CharField()),
            ],
        ),
    ]
