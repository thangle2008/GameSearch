from django.shortcuts import render
from . import utils

import os
import requests

MASHAPE_KEY = os.environ.get('MASHAPE_API_KEY')
GIANT_BOMB_KEY = os.environ.get('GIANT_BOMB_API_KEY')

# Create your views here.
def index(request):

    if request.method == "POST":
        # request data
        game_name = request.POST.get('game')

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

        return render(request, 'gamesearch/index.html', {'games': games})
    else:
        return render(request, 'gamesearch/index.html')