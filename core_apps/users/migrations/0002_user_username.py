# Generated by Django 4.1.7 on 2024-08-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                db_index=True,
                default=None,
                max_length=255,
                unique=True,
                verbose_name="نام کاربری",
            ),
        ),
    ]
