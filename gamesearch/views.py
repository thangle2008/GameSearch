from django.shortcuts import render
from utils import GBSearcher

import os

from django.core.cache import cache

def index(request):

    params = {}

    if request.method == "POST":
        # request data
        game_name = request.POST.get('game')

        cache_key = '_'.join(game_name.split())
        games = cache.get(cache_key)

        if games is None:
            print "request data on server"

            user_agent = request.META['HTTP_USER_AGENT']
            games = GBSearcher.search_by_name(game_name, user_agent)

            # cache the search results to reduce number of api requests
            cache.set(cache_key, games)

        params = {'games': games}

    return render(request, 'gamesearch/index.html', params)


def game(request, game_id):

    return render(request, 'gamesearch/game.html')