# Generated by Django 4.2.6 on 2023-10-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CloudKey",
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
                ("name", models.CharField(max_length=30)),
                ("key", models.TextField()),
                (
                    "cloudprovider",
                    models.CharField(
                        choices=[
                            ("Hetzner", "Hetzner"),
                            ("Google", "Google"),
                            ("AWS", "AWS"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SSHKey",
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
                ("name", models.CharField(max_length=30)),
                ("key", models.TextField()),
            ],
        ),
    ]
