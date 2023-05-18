from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
from django.db import transaction
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

@login_required(login_url="/admin/login/") #декоратор дает право на просмотр страницы только зарегестрированным поьзователям
def main_page(request):
    return render(request, 'main.html')

def place_arrangements (request):
    establishments = Establishments.objects.all()
    paginator = Paginator(establishments, 10)  # показывать кол-во друзей на странице.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "establishments": establishments,
        'page_obj': page_obj
    }

    return render(request, 'establishments.html', context=context)
    # context = {
    #     "establishments": Establishments.objects.all(),
    #
    # }
    # return render(request, 'establishments.html', context=context)

# @login_required(login_url="admin/login/")
# def main_page(request):
#     return render(request, 'main.html')

@permission_required('arrangement.view_users', login_url="/arrangement/main/") #наделяет правом просмотра данного раздела только зарегестрированным пользователям
def all_friends(request):
    users = Users.objects.all().prefetch_related("hobbies_set", "userrating_set")
    paginator = Paginator(users, 10)  # показывать кол-во друзей на странице.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "friends": users,
        'page_obj': page_obj
    }

    return render(request, 'friends.html', context=context)

@permission_required('arrangement.view_userrating', login_url="/arrangement/main/")
def user_rating(request):
    # context = {
    #     "ratings": UserRating.objects.all().select_related('user')
    # }
    users = UserRating.objects.all().select_related('user')
    paginator = Paginator(users, 10)  # показывать кол-во друзей на странице.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {

        "ratings": users,
        "page_obj": page_obj
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
                description=request.POST['description'],
                photo = request.FILES["photo"]
            )
            return redirect('user_rating')
    else:
        form = RatingUserForm()
        context['form'] = form


    return render(request, 'user_form_rating.html', context=context)

def create_user(request):
    context = {}
    if request.method == 'POST':
        form = CreateUserForm(request.POST,request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('friends')
    else:
        form = CreateUserForm()
        context['form'] = form


    return render(request, 'create_user_form.html', context=context)
@transaction.atomic
def make_arrangements(request):
    context = {}
    if request.method == "POST":
        form = ArrangementForm(request.POST)
        context["form"] = form
        guest = Guest.objects.all().order_by('?')[0]  #получаем случайного гостя
        if form.is_valid():  #проверяем валидность формы

            host_id = int(request.POST['host'][0]) # вытягиваем хоста по нулевому значению
            place_id = int(request.POST['place'][0])

            host = Host.objects.get(users_ptr_id=host_id)
            establishments = Establishments.objects.get(id=place_id)

            if host.status == 'a':
                host.status = 'b'
                host.save()
                Arrangements.objects.create(
                    host=host,
                    guest=Guest.objects.get(users_ptr_id=guest.id),
                    establishments=establishments
                )

            return redirect("friends")
    else:
        form = ArrangementForm()
        context["form"] = form

    return render(request, "make_arrangement.html", context=context)

        #     if host.status == 'a':
        #         host.status = 'b'
        #         host.save()
        #         Arrangements.objects.create(
        #             host=host,
        #             guest=Guest.objects.get(users_ptr_id=guest.id),
        #             establishments=establishments
        #         )
        #
        #         return redirect("friends")
        # else:
        #     form = ArrangementForm()
        #     context["form"] = form
        # return render(request, "make_arrangement.html", context=context)


def booking_place(request):
    context = {}
    if request.method == 'POST':
        form = BookingUserForm(request.POST)
        context['form'] = form
        if form.is_valid():

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

def static_url(request):
    return render(request, "static_example.html")

@login_required(login_url="/admin/login/")
def free_peoples(request):
    context = {
        "free_people": free_people,

    }
    return render(request, 'free_people.html', context=context)
@login_required(login_url="/admin/login/")
def busy_peoples(request):
    context = {
        "busy_people": busy_people,

    }
    return render(request, 'busy_people.html', context=context)

def dates (request):
    return render(request, 'date.html')


class PlaceListView(ListView):
    template_name = 'establishments.html'
    model = Establishments
    context_object_name = "establishments"
    queryset = Establishments.objects.all()

class EstablishmentsCreateView(LoginRequiredMixin,CreateView):
        template_name = 'createplace.html'
        login_url = "/admin/login/"  #просмотр только для зарегестрированных пользователей, иначе надо войти
        model = Establishments
        fields = ["name", "category", "address", "phone"]
        success_url = reverse_lazy("establishments")