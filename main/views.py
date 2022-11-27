from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.utils.timezone import now
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def searchres(request):
    if request.method == 'POST':
        form = PetitionSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pets = Petition.objects.filter(title__contains=data['title'])
            return render(request, 'main/searchres.html', {'pets': pets})
    else:
        return HttpResponseNotFound()


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                data['username'], data['email'], data['password'])
            u.save()
            p = Citizen(user=u, pin=data['pin'])
            p.save()
            return HttpResponse('Пользователь создан успешно!<br><a href="{% url \'index\' %}">На главную страницу</a>')
    else:
        form = UserRegForm()
    return render(request, 'main/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                return HttpResponse('Логин прошел успешно!<br><a href="{% url \'index\' %}">На главную страницу</a>')
            else:
                return HttpResponseNotFound()
    else:
        form = UserLogForm()
    return render(request, 'main/login.html', {'form': form})


def petition(request, id):
    if request.user.is_authenticated:
        pet = Petition.objects.get(id=id)
        com = Comment.objects.filter(petition=pet)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.author = request.user
                p.petition = pet
                p.time = now()
                p.save()
                p.save_m2m()
                return HttpResponse('Комментарий добавлен!')
        else:
            form = CommentForm()
        print(request.user)
        return render(request, 'main/petition.html', {'pet': pet, 'com': com, 'form': form})
    else:
        return HttpResponse(
            "Необходимо авторзоваться. <a href='/login/'>Ссылка</a>")


def index(request):
    popular = Petition.objects.order_by('votes')
    return render(request, 'main/index.html', {'popular': popular})
