# Generated by Django 4.2.5 on 2023-12-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("detector", "0005_remove_user_newuserid_alter_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="AttendanceFile",
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
                ("file_name", models.CharField(max_length=255)),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
