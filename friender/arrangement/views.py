from django.shortcuts import render

from django.http import HttpResponse
import datetime

friends = ['Max', 'Grigory', 'Pedro','Boris', 'Mihail']


# функция представления view(вьюшка)

def main_page(request,name):
    return HttpResponse(f"<h1>Hello {name}</h1>")


def all_friends (request):
    context = {
        "friends": friends,

    }
    return render(request,'friends.html',context=context)
