from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'ott_platforms', 'year', 'duration', 'imdb_rating', 'plot_description', 'genre', 'poster_url', 'trailer_url', 'movie_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].required = False
        self.fields['genre'].required = False
        self.fields['imdb_rating'].required = False