# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from main.views import index, all_busines, likes, likes_busines, all_filter_search, statistics

urlpatterns = [
    path('', index, name='index'),
    path('all_neighb/', all_filter_search, name='all_neighb'),
    # path('filter_search/', filter_search, name='filter_search'),

    path('all_busines/', all_busines, name='all_busines'),
    # path('search_busines/', filter_search_busines, name='search_busines'),
    path('likes/', likes, name='likes'),
    path('likes_busines/', likes_busines, name='likes_busines'),
    path('statistics/', statistics, name='statistics'),
]