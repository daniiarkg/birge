from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import *
from .forms import *
# Create your views here.


def searchres(request):
    if request.method == 'POST':
        form = PetitionSearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pets = Petition.objects.filter(title__startswith=data['title'])
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


def petition(request, id):
    pet = Petition.objects.get(id=id)
    return render(request, 'main/petition.html', {'pet': pet})


def index(request):
    popular = Petition.objects.order_by('votes')[:20 if len(
        Petition.objects.all()) > 20 else len(Petition.objects.all())]
    paginator = Paginator(popular, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj})
