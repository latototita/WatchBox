from django.contrib import admin
from django.urls import path
from .views import *
app_name='Vid'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', movie_detail, name='movie_detail'),
    path('video/<int:id>', stream_video, name='stream_video'),
    path('series', series_list, name='series_list'),
    path('kdrama', Kdrama, name='Kdrama'),
    path('Anime', Anime, name='Anime'),
    path('Animation', Animation, name='Animation'),
    path('series/<int:series_id>/', series_detail, name='series_detail'),
    path('episode/<int:episode_id>/download/', episode_download, name='episode_download'),
    path('episodes/<int:id>/stream/', episode_stream, name='episode_stream'),
]