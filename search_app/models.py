from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Chords(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(null=True, max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    legend = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.artist}) {self.genre} {self.rating}"