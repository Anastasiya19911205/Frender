from django.urls import path, re_path
from .views import *

#  маршрутизация
urlpatterns = [
    path('main/', main_page, name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', place_arrangements, name='establishments'),
    path('rules/', rules, name='rules'),
    path('static_url/', static_url, name="static_url"),
    path('user_rating/', user_rating, name="user_rating"),
    path('free_people/', free_peoples, name='free_people'),
    path('busy_people/', busy_peoples, name='busy_people'),
    path('date/', dates, name='date'),
    path('create_user/', create_user,name='create_user'),
    re_path(r"^rating_user/(?P<id>[0-9]+)$", user_form_rating,name='user_form_rating'),
    path('booking_place/', booking_place, name='booking_place'),
    path('comment_establishment/', comment_establishment, name='comment_establishment')

]
