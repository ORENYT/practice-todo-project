# Generated by Django 4.2.6 on 2023-10-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]