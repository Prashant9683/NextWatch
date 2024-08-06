# Generated by Django 5.0.3 on 2024-08-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0007_alter_movie_ott_platforms"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="duration",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="genre",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="plot_description",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="poster_url",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="year",
        ),
        migrations.AddField(
            model_name="movie",
            name="backdrop_path",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="movie",
            name="overview",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="poster_path",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="movie",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="runtime",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="vote_average",
            field=models.FloatField(blank=True, null=True),
        ),
    ]