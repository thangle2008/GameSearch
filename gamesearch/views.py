from django.shortcuts import render
from django.core.cache import cache

from .models import Game
from utils import GBSearcher

import os


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

            # add the games with their ratings to database
            for g in games:
                game_db, created = Game.objects.get_or_create(api_id=g['id'])

        params = {'games': games}

    return render(request, 'gamesearch/index.html', params)


def game(request, game_id):

    user_agent = request.META['HTTP_USER_AGENT']
    game = GBSearcher.search_by_id(game_id, user_agent)

    # concatenate game's genres and platforms
    get_name = lambda x: x['name']
    game['genres'] = ', '.join(map(get_name, game['genres']))
    game['platforms'] = ', '.join(map(get_name, game['platforms']))

    return render(request, 'gamesearch/game.html', {'game': game})