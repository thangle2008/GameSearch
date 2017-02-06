from django.shortcuts import render

import requests

# Create your views here.
def index(request):

    if request.method == "POST":
        game_name = request.POST.get('game')
        
        url = ("https://igdbcom-internet-game-database-v1.p.mashape.com/games/" 
                "?fields=name&limit=5&offset=0&order=release_dates.date%3Adesc&"
                "search={}".format(game_name))

        headers = {'X-Mashape-Key': 'smWYagZHkJmshRNBatAZHwsN4eCdp1RvuPcjsnANdEgkyyu8lq'}

        r = requests.get(url, headers=headers)
        
        return render(request, 'gamesearch/index.html', {'games': r.json()})
    else:
        return render(request, 'gamesearch/index.html')