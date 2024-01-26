# Generated by Django 5.0 on 2024-01-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questionpaper", "0009_alter_multiplechoicequestion_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiplechoicequestion",
            name="mcq",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="multiplechoicequestion",
            name="subject",
            field=models.CharField(
                choices=[
                    ("", "--select--"),
                    ("islamiyat", "Islamiyat"),
                    ("urdu", "Urdu"),
                    ("physics", "Physics"),
                    ("chemistry", "Chemsitry"),
                    ("bioloby", "Biology"),
                    ("math", "Mathematics"),
                    ("english", "English"),
                    ("pakstudy", "Pakistan Study"),
                ],
                default="--select--",
                max_length=20,
            ),
        ),
    ]
