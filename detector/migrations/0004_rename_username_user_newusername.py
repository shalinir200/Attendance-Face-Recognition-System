# Generated by Django 4.2.5 on 2023-12-24 16:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("detector", "0003_rename_add_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="username",
            new_name="newusername",
        ),
    ]