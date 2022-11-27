from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('petition/<int:id>', views.petition, name='petition'),
    path('registration/', views.register, name='registration'),
    path('searchres/', views.searchres, name='searchres'),
    path('login/', views.login, name='login')
]
