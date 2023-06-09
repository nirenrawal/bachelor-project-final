# Generated by Django 4.2.1 on 2023-06-16 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_registration", "0003_alter_userinfo_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userinfo",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
