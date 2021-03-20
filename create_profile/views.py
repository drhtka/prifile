# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from create_profile.forms import CreateForms, CreateFormsB
from create_profile.models import CreateNeighbour, CreateBusiness

# Create your views here.
def create_neighbour(request):
    # страница добавления соседа
    all_ancets = CreateNeighbour.objects.filter(user_neig=request.user.id).values_list()
    form = ''
    if request.method == 'POST':
        form = CreateForms(request.POST, request.FILES)
        if form.is_valid():
            create_post = form.save(commit=False)
            if request.user.is_authenticated:
                create_post.user_neig = request.user

            create_post.save()
            return redirect('/all_neighb/')
    else:
        if len(all_ancets) > 0:
            # print('1')
            # button_vis = 'un_visible'
            return redirect('/all_neighb/')
        else:
            form = CreateForms
    return render(request, 'neighbour.html', {'form': form})

def create_business(request):
    # страница добавления бизнес
    all_ancets = CreateBusiness.objects.filter(user_bus=request.user.id).values_list()
    form = ''
    if request.method == 'POST':
        form = CreateFormsB(request.POST, request.FILES)
        if form.is_valid():
            create_post = form.save(commit=False)
            if request.user.is_authenticated:
                create_post.user_bus = request.user
            create_post.save()
            return redirect('/all_busines/')
    else:
        if len(all_ancets) > 0:
            # print('1')
            # button_vis = 'un_visible'
            return redirect('/all_busines/')
        else:
            form = CreateFormsB
    return render(request, 'business.html',  {'form': form})