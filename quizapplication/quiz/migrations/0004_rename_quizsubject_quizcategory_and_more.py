# Generated by Django 4.2.1 on 2023-05-31 07:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0003_remove_question_description_quizsubject_description"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="QuizSubject",
            new_name="QuizCategory",
        ),
        migrations.AlterModelOptions(
            name="quizcategory",
            options={"verbose_name_plural": "quiz catogeries"},
        ),
    ]
