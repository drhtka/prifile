# -*- coding: utf-8 -*-

from django.forms import ModelChoiceField
from django.shortcuts import render, redirect
from create_profile.forms import CreateForms, CreateFormsB
from create_profile.models import CreateNeighbour, CreateBusiness, AllCities
from mptt.forms import MoveNodeForm

# Create your views here.
def create_neighbour(request):
    # страница добавления соседа
    # category = ModelChoiceField(queryset=AllCities.objects.all(parent_id=None))
    # print('category')
    # print(category.queryset)

    all_ancets = CreateNeighbour.objects.filter(user_neig=request.user.id)
    print('allCities-12')
    allCities = AllCities.objects.filter(parent_id=None).values('id', 'name')
    print('allCities-13')
    print(allCities)
    form = ''
    if request.method == 'POST':

        form = CreateForms(request.POST, request.FILES)
        cities = AllCities.objects.filter(id=request.POST.get('cities')).values('name')
        regin = AllCities.objects.filter(id=request.POST.get('regin')).values('name')
        if form.is_valid():
            create_post = form.save(commit=False)
            if request.user.is_authenticated:
                create_post.user_neig = request.user
                create_post.cities=cities[0]['name']
                create_post.regin=regin[0]['name']
            print('create_post-61')
            print(create_post)
            create_post.save()
            return redirect('/all_neighb/')
    else:
        if len(all_ancets) > 0:
            # print('1')
            # button_vis = 'un_visible'
            return redirect('/all_neighb/')
        else:
            form = CreateForms

    return render(request, 'neighbour.html', {'form': form, 'allCities':allCities})

def create_business(request):
    # страница добавления бизнес

    all_ancets = CreateBusiness.objects.filter(user_bus=request.user.id).values_list()
    allCities = AllCities.objects.filter(parent_id=None).values('id', 'name')
    print('45')
    # print(request.POST.get('regin'))
    # allCities_reg = AllCities.objects.filter(id=request.POST.get('regin')).values('id')
    #
    print('cities-50')
    # print(allCities_reg[0]['id'])
    print(request.POST.get('cities'))
    print(request.POST.get('regin'))

    form = ''
    if request.method == 'POST':
        print('helo post')
        form = CreateFormsB(request.POST, request.FILES)
        cities = AllCities.objects.filter(id=request.POST.get('cities')).values('name')
        regin = AllCities.objects.filter(id=request.POST.get('regin')).values('name')
        print('cities-61')
        print(cities[0]['name'], regin[0]['name'])
        # category_bus.save()
        print('request.POST-52')
        print(request.POST)
        if form.is_valid():
            print('1')
            create_post = form.save(commit=False)
            if request.user.is_authenticated:
                create_post.user_bus = request.user
                create_post.cities=cities[0]['name']
                create_post.regin=regin[0]['name']
            print('create_post-61')
            print(create_post)
            create_post.save()

            return redirect('/all_busines/')
    else:
        if len(all_ancets) > 0:
            # print('1')
            # button_vis = 'un_visible'
            return redirect('/all_busines/')
        else:
            form = CreateFormsB
    return render(request, 'business.html',  {'form': form, 'allCities': allCities})