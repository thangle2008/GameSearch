from django.shortcuts import render
from . import utils

import os
import requests

MASHAPE_KEY = os.environ.get('MASHAPE_API_KEY')

# Create your views here.
def index(request):

    if request.method == "POST":
        # request data using IGDB API
        game_name = request.POST.get('game')
        url = ("https://igdbcom-internet-game-database-v1.p.mashape.com/games/" 
                "?fields=*&limit=10&offset=0"
                "&order=release_dates.date%3Adesc"
                "&search={}".format(game_name))
        headers = {'X-Mashape-Key': MASHAPE_KEY}

        r = requests.get(url, headers=headers)

        # process data
        games = r.json()
        for g in games:
            if 'rating' in g: g['rating'] = utils.score_to_star(g['rating'])
        
        return render(request, 'gamesearch/index.html', {'games': games})
    else:
        return render(request, 'gamesearch/index.html')