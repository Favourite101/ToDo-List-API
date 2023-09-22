# Generated by Django 4.2.5 on 2023-09-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDoList",
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
                ("Title", models.CharField(max_length=100)),
                ("Description", models.TextField(blank=True)),
                ("Date", models.DateField()),
                ("Completed", models.BooleanField(default=False)),
            ],
        ),
    ]
