# Generated by Django 5.0.3 on 2024-08-06 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0017_alter_movie_tmdb_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="imdb_rating",
            field=models.DecimalField(
                decimal_places=1,
                default=0.0,
                max_digits=3,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(10.0),
                ],
            ),
        ),
    ]
