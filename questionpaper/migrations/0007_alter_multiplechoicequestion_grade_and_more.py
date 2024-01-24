# Generated by Django 5.0 on 2024-01-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questionpaper", "0006_multiplechoicequestion_grade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiplechoicequestion",
            name="grade",
            field=models.CharField(
                choices=[
                    ("", "--select--"),
                    ("10", "10"),
                    ("9", "9"),
                    ("8", "8"),
                    ("7", "7"),
                    ("6", "6"),
                    ("5", "5"),
                ],
                default="--select--",
                max_length=20,
            ),
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