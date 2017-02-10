from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Game(models.Model):
    api_id = models.IntegerField(primary_key=True)
    score = models.FloatField(default=0)
    n_reviews = models.IntegerField(default=0)

    def add_score(self, score):
        """Update the average score of this game."""

        if score <= 5.0:
            self.score = self.score * self.n_reviews + score
            self.n_reviews += 1
            self.score /= self.n_reviews