# Generated by Django 5.0 on 2024-02-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="img",
            field=models.ImageField(
                blank=True, default="default_pic.jpg", upload_to="images"
            ),
        ),
    ]
