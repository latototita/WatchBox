from django.urls import path
from .views import MovieList, MovieDetail, SeriesList, SeriesDetail,MovieUploadView, SeriesUploadView
app_name='api'
urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('series/', SeriesList.as_view(), name='series-list'),
    path('series/<int:pk>/', SeriesDetail.as_view(), name='series-detail'),
    path('movies/upload/', MovieUploadView.as_view(), name='movie-upload'),
    path('series/upload/', SeriesUploadView.as_view(), name='series-upload'),
]