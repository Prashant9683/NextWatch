from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    ott_platforms = models.CharField(max_length=200, default='NONE')
    imdb_rating = models.FloatField()
    plot_description = models.TextField()
    genre = models.CharField(max_length=100)
    poster_url = models.URLField()
    watched = models.BooleanField(default=False)
    year = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)
    trailer_url = models.URLField(blank=True, null=True)
    movie_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title