from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_page, name='movies_page'),
    path('api/movies/new/', views.new_movies_api, name='new_movies_api'),
]
