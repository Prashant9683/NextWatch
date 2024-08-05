from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Movie
from .forms import MovieForm
from django.db.models import Q


def duration_to_minutes(duration_str):
    parts = duration_str.split()
    total_minutes = 0
    for part in parts:
        if part.endswith('h'):
            hours = int(part[:-1])
            total_minutes += hours * 60
        elif part.endswith('m'):
            minutes = int(part[:-1])
            total_minutes += minutes
    return total_minutes

def search_movies(request):
    search_query = request.GET.get('search', '')
    movies = Movie.objects.all()

    if search_query:
        movies = movies.filter(title__icontains=search_query)

    return render(request, 'movies/movie_search_results.html', {
        'movies': movies,
        'search_query': search_query,
    })

def movie_list(request):
    movies = Movie.objects.all().order_by('-year')

    # Filter by year
    year = request.GET.get('year')
    if year:
        movies = movies.filter(year=year)
    static_genres = [
        "Action", "Adventure", "Animation", "Biography", "Comedy", 
        "Crime", "Documentary", "Drama", "Family", "Fantasy", 
        "History", "Horror", "Music", "Musical", "Mystery", 
        "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"
    ]
    # Filter by genre
    genre = request.GET.get('genre')
    if genre:
        movies = movies.filter(Q(genre__icontains=genre))
    # Filter by IMDb rating
    min_rating = request.GET.get('min_rating')
    max_rating = request.GET.get('max_rating')
    if (min_rating and max_rating):
        movies = movies.filter(imdb_rating__gte=min_rating, imdb_rating__lte=max_rating)
    elif min_rating:
        movies = movies.filter(imdb_rating__gte=min_rating)
    elif max_rating:
        movies = movies.filter(imdb_rating__lte=max_rating)
    # Sort movies
    sort_by = request.GET.get('sort_by')
    if sort_by == 'year':
        movies = movies.order_by('-year')
    elif sort_by == 'rating':
        movies = movies.order_by('-imdb_rating')
    elif sort_by == 'duration':
        movies = sorted(movies, key=lambda x: duration_to_minutes(x.duration))
    elif sort_by == 'title':
        movies = movies.order_by('title')
    years = Movie.objects.values_list('year', flat=True).distinct()
    genres = Movie.objects.values_list('genre', flat=True).distinct()

    return render(request, 'movies/movie_list.html', {'movies': movies, 'years': years, 'genres': genres, 'static_genres': static_genres})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/update_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/delete_movie.html', {'movie': movie})

def toggle_watched(request, pk):
    print(f"Toggle watched called for movie {pk}")
    movie = get_object_or_404(Movie, pk=pk)
    movie.watched = not movie.watched
    movie.save()
    return render(request, 'movies/movie_detail.html', {'movie': movie})