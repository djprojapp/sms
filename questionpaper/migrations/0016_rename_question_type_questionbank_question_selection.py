# Generated by Django 5.0 on 2024-01-30 07:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("questionpaper", "0015_questionselection_questionbank_chapter_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questionbank",
            old_name="question_type",
            new_name="question_selection",
        ),
    ]
