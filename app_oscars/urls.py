from django.contrib import admin
from django.urls import path
from app_oscars.views import ranking, films_rating,new_film, edit_film, delete_film, ReviewListView, films
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('ranking/',ReviewListView.as_view(), name="ranking"),
   path('new_film/',new_film, name="new_film"),
   path('edit_film/<int:id>',edit_film, name="edit_film"),
   path('delete_film/<int:id>',delete_film, name="delete_film"),
   path('films_rating/<int:id>', films_rating, name="films_rating"),
   path('films/',films, name="films"),

]
