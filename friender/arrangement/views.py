from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
from django.core.paginator import Paginator
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
        "establishments": Establishments.objects.all(),

    }
    return render(request, 'establishments.html', context=context)


def all_friends(request):
    # users = Users.objects.all()
    # paginator = Paginator(users, 20)  # Show 25 contacts per page.
    #
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    context = {
        "friends": Users.objects.all()[:40]
        # "page_obj" = page.obj
    }

    return render(request, 'friends.html', context=context)

def static_url(request):
    return render(request, "static_example.html")

def user_rating(request):
    context = {
        "ratings": UserRating.objects.all().select_related('user')
    }
    return render(request, 'user_rating.html', context=context)

def user_form_rating(request,**kwargs):
    user_id = int(kwargs['id'])
    context = {}
    if request.method == 'POST':
        form = RatingUserForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            UserRating.objects.create(
                user_id=user_id,
                rating=request.POST['rating'],
                description=request.POST['description']
            )
            return redirect('user_rating')
    else:
        form = RatingUserForm()
        context['form'] = form


    return render(request, 'user_form_rating.html', context=context)

def create_user(request):
    context = {}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('friends')
    else:
        form = CreateUserForm()
        context['form'] = form


    return render(request, 'create_user_form.html', context=context)





def booking_place(request):
    context = {}
    if request.method == 'POST':
        form = BookingUserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('friends')
    else:
        form = BookingUserForm()
        context['form'] = form


    return render(request, 'booking_place.html', context=context)

def comment_establishment(request):
    context = {}
    if request.method == 'POST':
        form = CommentEstUserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            return redirect('friends')
    else:
        form = CommentEstUserForm()
        context['form'] = form

    return render(request, 'comment_establishment.html', context=context)
def rules(request):
    return render(request, 'rules.html')


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
