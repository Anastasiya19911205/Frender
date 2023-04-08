from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Users
import datetime

# friends = {
#     'Max': [34, "Max@mail.ru"],
#     'Grigory': [32, "Grigory@mail.ru"],
#     "Anna": [29, "Anna@mail.ru"],
#     'Pedro': [21, "Pedro@mail.ru"],
#     "Kate": [34, "Kate@mail.ru"]
#    }

establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Pancakes', 'Depo']

free_people = {
    'Angelina': [25, "Angelina@mail.ru"],
    'Alexei': [28, "Alexei@mail.ru"],
    'Marina': [26, "Marina@mail,ru"],
    "Roma": [29, "Roma@mail.ru"]

}

busy_people = {
    'Grisha': [48, "Grisha@mail.ru"],
    "Anniuta": [27, "Anniuta@mail.ru"],
    'Radion': [21, "Radion@mail.ru"],
    "Katerina": [30, "Katerina@mail.ru"]

}
# функция представления view(вьюшка)

def main_page(request):
    return render(request, 'main.html')

def place_arrangements (request):
    context = {
        "establishments": establishments,

    }
    return render(request, 'establishments.html', context=context)


def all_friends (request):
    context = {
        "friends": Users.objects.all(),

    }
    return render(request, 'friends.html', context=context)

def static_url(request):
    return render(request, "static_example.html")

def rules(request):
    return render(request, 'rules.html')

# def static_url(request):
#     return render(request, "static_example.html")

def free_peoples(request):
    context = {
        "free_people": free_people,

    }
    return render(request, 'free_people.html', context=context)

def busy_peoples(request):
    context = {
        "busy_people": busy_people,

    }
    return render(request, 'busy_people.html', context=context)

def dates (request):
    return render(request, 'date.html')
