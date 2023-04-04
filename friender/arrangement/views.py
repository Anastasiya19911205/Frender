from django.shortcuts import render

from django.http import HttpResponse
import datetime

friends = ['Max', 'Grigory', 'Pedro','Boris', 'Mihail']
establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Pancakes', 'Depo']

# функция представления view(вьюшка)

def main_page(request):
    return render( request, 'main.html')

def place_arrangement (reguest):
    return render(request, 'establishments.html')


def all_friends (request):
    context = {
        "friends": friends,

    }
    return render(request,'friends.html',context=context)
