import requests

from django.conf import settings

# Helper functions

def score_to_star(score):
    """
    Convert a double score rating (0-100) to star rating (0-5)
    """
    return int(round(score / 20.0))


class GBSearcher():
    """
    A searcher for games on Giantbomb.
    """

    @staticmethod
    def search_by_name(name, user_agent, limit=5):
        """
        Search for a list of games by name.
        """

        base_url = 'http://www.giantbomb.com/api/games'
        params = {
            'api_key': settings.GIANT_BOMB_KEY,
            'format': 'json',
            'filter': 'name:{}'.format(name),
            'limit': 5
        }
        headers = {'User-Agent': user_agent}

        r = requests.get(base_url, headers=headers, params=params)
        games = r.json()['results']

        return games

    @staticmethod
    def search_by_id(id, user_agent):
        """
        Search for a game by id.
        """

        base_url = 'http://www.giantbomb.com/api/game/3030-{}'.format(id)

        params = {
            'api_key': settings.GIANT_BOMB_KEY,
            'format': 'json',
        }
        headers = {'User-Agent': user_agent}

        r = requests.get(base_url, headers=headers, params=params)
        game = r.json()['results']

        return game