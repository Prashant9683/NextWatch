from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    ott_platforms = models.CharField(max_length=200, default='NONE')
    imdb_rating = models.DecimalField(
            max_digits=3, 
            decimal_places=1, 
            default=0.0,
            validators=[
                MinValueValidator(0.0),
                MaxValueValidator(10.0)
            ]
        )
    plot_description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100, default='NONE')
    poster_url = models.URLField(blank=True, null=True)
    watched = models.BooleanField(default=False)
    year = models.IntegerField(default=0)
    duration = models.CharField(max_length=20, default='0h 0m')
    trailer_url = models.URLField(blank=True, null=True)
    movie_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title