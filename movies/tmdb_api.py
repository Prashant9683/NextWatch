import requests
from django.conf import settings

TMDB_API_KEY = settings.TMDB_API_KEY
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }
    response = requests.get(url, params=params)
    return response.json()

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "append_to_response": "credits"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_tmdb_movie_providers(tmdb_id):
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/watch/providers'
    params = {
        'api_key': TMDB_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Assuming you want the US providers; adjust the region as needed
    providers = data.get('results', {}).get('US', {}).get('flatrate', [])
    provider_names = [provider['provider_name'] for provider in providers]
    
    return provider_names