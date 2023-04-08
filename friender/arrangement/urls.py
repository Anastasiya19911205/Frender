from django.urls import path
from .views import *

#  маршрутизация
urlpatterns = [
    path('main/', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', place_arrangements, name='establishments'),
    path('rules/', rules, name='rules'),
    path('static_url/', static_url, name="static_url"),
    path('free_people/', free_peoples, name='free_people'),
    path('busy_people/', busy_peoples, name='busy_people'),
    path('date/', dates, name='date')
]
