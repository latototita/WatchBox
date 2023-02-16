from main.models import *
from .serializers import MovieSerializer, SeriesSerializer
from rest_framework import generics, permissions, parsers


class MovieUploadView(generics.CreateAPIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SeriesUploadView(generics.CreateAPIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SeriesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class MovieList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = MovieSerializer

class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer