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

        params = {'games': games}

    return render(request, 'gamesearch/index.html', params)


def game(request, game_id):

    game, created = Game.objects.get_or_create(api_id=game_id)

    # if this game is not in the database
    if created:
        print "request data on server"

        user_agent = request.META['HTTP_USER_AGENT']
        game_info = GBSearcher.search_by_id(game_id, user_agent)

        game.name = game_info['name']
        game.summary = game_info['deck']
        game.cover_img = game_info['image']['super_url']

        # concatenate game's genres and platforms
        get_name = lambda x: x['name']
        game.genres = ', '.join(map(get_name, game_info['genres']))
        game.platforms = ', '.join(map(get_name, game_info['platforms']))

        game.save()

    return render(request, 'gamesearch/game.html', {'game': game})