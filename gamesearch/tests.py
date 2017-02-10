from django.test import TestCase

from .models import Game

# Create your tests here.
class GameMethodTest(TestCase):

    def setUp(self):
        Game.objects.create(api_id=2)
        Game.objects.create(api_id=3)

    def test_add_score(self):
        g = Game.objects.get(api_id=2)

        # default values
        self.assertEqual(g.score, 0.0)
        self.assertEqual(g.n_reviews, 0)

        g.add_score(10.0)
        self.assertEqual(g.score, 0.0)
        self.assertEqual(g.n_reviews, 0)

        g.add_score(5.0)
        self.assertEqual(g.score, 5.0)
        self.assertEqual(g.n_reviews, 1)

        g.add_score(4.0)
        self.assertEqual(g.score, 4.5)
        self.assertEqual(g.n_reviews, 2)  