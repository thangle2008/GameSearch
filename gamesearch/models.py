from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    """A genre's information, including which game has this genre."""

    api_id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Game(models.Model):
    """A game's information."""

    api_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    score = models.FloatField(default=0)
    n_reviews = models.IntegerField(default=0)
    cover_img = models.URLField()
    genres = models.ManyToManyField(Genre)

    def add_score(self, score):
        """Update the average score of this game."""

        if score <= 5.0:
            self.score = self.score * self.n_reviews + score
            self.n_reviews += 1
            self.score /= self.n_reviews
