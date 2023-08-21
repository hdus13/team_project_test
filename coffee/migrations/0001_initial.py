# Generated by Django 4.2.4 on 2023-08-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coffee",
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
                ("brand", models.CharField(max_length=10)),
                ("coffee", models.CharField(max_length=20)),
                ("coffee_name", models.CharField(max_length=20)),
            ],
        ),
    ]
