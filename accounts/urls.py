# -*- coding: utf-8 -*-
from django.urls import path, include

from accounts.views import register_view


urlpatterns = [
    path('register/', register_view, name='register'),
]