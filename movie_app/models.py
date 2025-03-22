from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class User(AbstractUser):
    is_active = models.BooleanField(default=False)

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_code():
        return ''.join(random.choices('0123456789', k=6))

class AbstractNameMode(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Director(AbstractNameMode):
    parent = models.ForeignKey('self', on_delete=models.CASCADE
                               , null=True, blank=True)
    pass


class Tag(AbstractNameMode):
    pass

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    release_year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def director_name(self):
        return self.director.name if self.director else None


STARS = (
    (i, '* ', * i) for i in range(1, 6)
)


class Review(models.Model):
    text = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)

    def __str__(self):
        return self.text


