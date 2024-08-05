from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:pk>/', views.update_movie, name='update_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
    path('toggle_watched/<int:pk>/', views.toggle_watched, name='toggle_watched'),
]