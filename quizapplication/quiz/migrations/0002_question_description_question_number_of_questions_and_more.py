# Generated by Django 4.2.1 on 2023-05-30 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="description",
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name="question",
            name="number_of_questions",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="question",
            name="time",
            field=models.IntegerField(default=1, help_text="Duration in Seconds"),
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("content", models.CharField(max_length=200)),
                ("correct_answer", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="quiz.question"
                    ),
                ),
            ],
        ),
    ]
