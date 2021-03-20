# -*- coding: utf-8 -*-
from django import forms
# from django.contrib.auth import get_user_model, authenticate
#
# User = get_user_model()
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}), max_length=12)
    first_name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}), max_length=50)
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'}), max_length=35)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'Registration_field__GURFO', 'placeholder': 'пароль'}), max_length=20)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'Registration_field__GURFO', 'placeholder': 'пароль еще раз'}), max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password2']

