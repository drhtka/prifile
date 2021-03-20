# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from accounts.views import register_view
from create_profile.views import create_neighbour, create_business
app_name = 'create'

urlpatterns = [
    path('neighbour/', create_neighbour, name='neighbour'),
    path('business/', create_business, name='business'),
    # path('register/', register_view, name='register'),
]