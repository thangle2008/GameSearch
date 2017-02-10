from django.shortcuts import render
from . import utils

import os
import requests

from django.core.cache import cache

MASHAPE_KEY = os.environ.get('MASHAPE_API_KEY')
GIANT_BOMB_KEY = os.environ.get('GIANT_BOMB_API_KEY')

# Create your views here.
def index(request):

    if request.method == "POST":
        # request data
        game_name = request.POST.get('game')

        cache_key = '_'.join(game_name.split())
        games = cache.get(cache_key)

        if games is None:
            print "request data on server"

            base_url = 'http://www.giantbomb.com/api/games'
            params = {
                'api_key': GIANT_BOMB_KEY,
                'format': 'json',
                'filter': 'name:{}'.format(game_name),
                'limit': 5
            }
            headers = {'User-Agent': request.META['HTTP_USER_AGENT']}

            r = requests.get(base_url, headers=headers, params=params)
            games = r.json()['results']

            # cache the search results to reduce number of api requests
            cache.set(cache_key, games)

        return render(request, 'gamesearch/index.html', {'games': games})
    else:
        return render(request, 'gamesearch/index.html')