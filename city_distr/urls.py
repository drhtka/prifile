# -*- coding: utf-8 -*-
from django.contrib import admin

from django.urls import path, include

from city_distr import views


urlpatterns = [

    path('city_distr/', views.show_genres, name='city_distr')

]


