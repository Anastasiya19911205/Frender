from django.urls import path
from .views import *

#  маршрутизация
urlpatterns = [
    path('main', main_page),
    path ('friends', all_friends),
    path ('establishments', place_arrangement)

]
