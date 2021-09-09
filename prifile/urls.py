# -*- coding: utf-8 -*-
"""prifile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views
from main.views import tree_form, search_fetch, tree_form_b, search_fetch_b


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('create/', include('create_profile.urls')),
    path('', include('city_distr.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('tree_form', tree_form,),
    path('tree_form_b', tree_form_b,),
    path('search_fetch', search_fetch, name='search_fetch'),
    path('search_fetch_b', search_fetch_b, name='search_fetch_b'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://stackoverflow.com/questions/41883254/django-is-not-a-registered-namespace/41883421
# path('create/', include('create_profile.urls', namespace='create')),