from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewsSerializer

# Director views
class DirectorListAPIView(generics.ListCreateAPIView):  # Изменено на ListCreateAPIView
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # Изменено на RetrieveUpdateDestroyAPIView
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# Movie views
class MovieListAPIView(generics.ListCreateAPIView):  # Изменено на ListCreateAPIView
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # Изменено на RetrieveUpdateDestroyAPIView
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Review views
class ReviewListAPIView(generics.ListCreateAPIView):  # Изменено на ListCreateAPIView
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # Изменено на RetrieveUpdateDestroyAPIView
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Существующий класс для отзывов к фильмам
class MovieReviewsListAPIView(generics.ListAPIView):
    queryset = Movie.objects.prefetch_related('review_set').all()
    serializer_class = MovieReviewsSerializer