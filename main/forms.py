from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PetitionSearchForm(forms.Form):
    title = forms.CharField(label='Поиск петиций', max_length=60)


class PetitionForm(ModelForm):
    class Meta:
        model = Petition
        fields = ['title', 'text']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class UserLogForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=40)
    password = forms.CharField(
        label='Пароль', max_length=50, widget=forms.PasswordInput)


class UserRegForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=40)
    email = forms.EmailField(label='E-mail')
    pin = forms.CharField(label='ПИН', max_length=14)
    password = forms.CharField(
        label='Пароль', max_length=50, widget=forms.PasswordInput)
    password_valid = forms.CharField(
        label='Пароль', max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cl_data = super().clean()
        passw = cl_data.get('password')
        passw_val = cl_data.get('password_valid')
        if passw != passw_val:
            raise ValidationError('Пароли не совпадают')
        if self.pin[0] not in ['1', '2'] or int(self.pin[1:3]) > 31 or int(self.pin[3:5]) > 2500:
            raise ValidationError('Неправильный формат ПИНа')
