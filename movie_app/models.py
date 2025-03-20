from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # в минутах
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1
    )