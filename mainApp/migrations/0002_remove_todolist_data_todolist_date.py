# Generated by Django 4.2.5 on 2023-09-19 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="todolist", name="Data",),
        migrations.AddField(
            model_name="todolist",
            name="Date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
