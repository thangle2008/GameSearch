from django.conf.urls import url
from . import views

app_name = 'gamesearch'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<game_id>[0-9]+)/$', views.game, name='game'),
]