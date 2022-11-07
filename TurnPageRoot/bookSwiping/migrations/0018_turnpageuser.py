# Generated by Django 4.1.2 on 2022-11-01 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookSwiping", "0017_rename_users_list_book_users_liked_list"),
    ]

    operations = [
        migrations.CreateModel(
            name="TurnPageUser",
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
                (
                    "liked_books",
                    models.ManyToManyField(
                        blank=True, related_name="liked_books", to="bookSwiping.book"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
