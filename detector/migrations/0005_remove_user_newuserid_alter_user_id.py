# Generated by Django 4.2.5 on 2023-12-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("detector", "0004_rename_username_user_newusername"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="newuserid",
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
