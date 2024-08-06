from tmdbv3api import TMDb, Movie
from django.conf import settings

tmdb = TMDb()
tmdb.api_key = settings.TMDB_API_KEY

def search_tmdb_movies(query):
    movie = Movie()
    return movie.search(query)

def get_tmdb_movie_details(tmdb_id):
    movie = Movie()
    return movie.details(tmdb_id)