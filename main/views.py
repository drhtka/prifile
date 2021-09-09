# -*- coding: utf-8 -*-
import math

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy

from create_profile.forms import CreateFormsB
from create_profile.models import CreateNeighbour, CreateBusiness, LikeModel, LikeBusinesModel, AllCities#, \
    #Profession  # , LikeEndModelNe


def index(request):
    # Главная
    if request.user.is_authenticated:

        # при авторизации сообщение пользоваиелям у кого встречные лайки соседей
        all_likes = LikeModel.objects.filter(like_second=request.user).values('like_first')
        for all_likes_s in all_likes:
            # print('all_likes-Neighb')
            # print(all_likes)
            step_one = []
            step_two = []
            if len(all_likes) > 0:
                # print('шаг1 нашел')
                step_one = all_likes_s
                # шаг 2
                all_likes_two = LikeModel.objects.filter(like_first=request.user).values('like_second')
                if len(all_likes_two) > 0:
                    # print('шаг 2 нашел')
                    # print(all_likes_two)
                    step_two = all_likes_two
                    # ii = int(0)
                    # print('step_one :', step_one)
                    # print('step_two :', step_two)
                    for step_two_s in step_two:
                        if step_two_s['like_second'] == step_one['like_first']:

                            messages.success(request, 'Вас лайкнул пользователь: ' + step_two_s['like_second'])
                            email_second = LikeModel.objects.filter(like_second=step_two_s['like_second']).values('email_second')
                            messages.success(request, ' Напишите ему: ' + email_second[0]['email_second'])



        all_likes_b = LikeBusinesModel.objects.filter(like_second=request.user).values()
        for all_likes_s_b in all_likes_b:
            step_one_b = []
            step_two_b = []
            if len(all_likes_b) > 0:
                if len(all_likes_b) > 0:
                    step_one_b = all_likes_s_b
                    all_likes_b_two = LikeBusinesModel.objects.filter(like_first=request.user).values('like_second')
                    if len(all_likes_b_two) > 0:
                        step_two_b = all_likes_b_two

                        for all_likes_s_b_s in step_two_b:
                            if all_likes_s_b_s['like_second'] == step_one_b['like_first']:
                                messages.success(request, 'Вас лайкнул бизнес пользователь: ' + all_likes_s_b_s['like_second'])
                                email_second_b = LikeBusinesModel.objects.filter(like_second=all_likes_s_b_s['like_second']).values('email_second')
                                messages.success(request, 'Почта для связи: ' + email_second_b[0]['email_second'])

        return render(request, 'index.html',)
    else:
        return render(request, 'index.html', )

@login_required(login_url=reverse_lazy('login'))
def all_filter_search(request):
    # выводим все анкеты
    list_tmp_13 = 0

    allCities = AllCities.objects.all()
    catalog_filter = CreateNeighbour.objects.values_list('id',
                                                          'name',
                                                          'gender',
                                                          'gender_neighb',
                                                          # 'sel_city',
                                                          # 'sel_distr',
                                                          'presence_animals',
                                                          'presence_flat',
                                                          'attitude_animals',
                                                          'attitude_smok',
                                                          'about_me',
                                                          'image',
                                                          'user_neig',
                                                          'cities',
                                                          'regin',)

    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    # формируем масив лдя прорисовки в шблоне
    for all_goods_s in catalog_filter:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateNeighbour(gender=tmp_s[2])
            gender = p.get_gender_display()

            p = CreateNeighbour(gender_neighb=tmp_s[3])
            gender_neighb = p.get_gender_neighb_display()

            # p = CreateNeighbour(sel_city=tmp_s[4])
            # sel_city = p.get_sel_city_display()
            #
            # p = CreateNeighbour(sel_distr=tmp_s[5])
            # sel_distr = p.get_sel_distr_display()

            p = CreateNeighbour(attitude_animals=tmp_s[6])
            attitude_animals = p.get_attitude_animals_display()

            p = CreateNeighbour(attitude_smok=tmp_s[7])
            attitude_smok = p.get_attitude_smok_display()

            cities_name = AllCities.objects.filter(name=tmp_s[11]).values('name')
            distr_name = AllCities.objects.filter(name=tmp_s[12]).values('name')
            # cities_b = p.get_cities_b_display()
            # print('allCities_name')
            #
            # print(cities_name[0]['name'])
            # print(distr_name[0]['name'])

            list_tmp = list(tmp_s)
            list_tmp[2] = gender
            list_tmp[3] = gender_neighb
            # list_tmp[4] = sel_city
            # list_tmp[5] = sel_distr
            list_tmp[6] = attitude_animals
            list_tmp[7] = attitude_smok

            list_tmp[11] = cities_name[0]['name']
            list_tmp[12] = distr_name[0]['name']
            user_like = LikeModel.objects.filter(first_id=tmp_s[10]).filter(second_id=request.user.id).values_list('id') # лайки в шаблоне
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)

            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list) # формируем массив со всеми анкетами
        # print('allCities')
        # print(allCities)

    return render(request, 'all_neighb.html', {'serxh_filer': tmp_categ_name, 'allCities': allCities,})

@login_required(login_url=reverse_lazy('login'))
def all_busines(request):
    # весь бизнес
    # формируем массив со всеми анкетами
    distinr = CreateBusiness.objects.order_by('category_bus').values('category_bus').distinct()
    print('distin254')
    print(distinr)
    allCities = AllCities.objects.all()
    form = CreateFormsB()
    search_filer = CreateBusiness.objects.values_list('name_bus',
                                                       # 'sel_city',
                                                       # 'sel_distr',
                                                       'category_bus',
                                                       'about_me',
                                                       'image',
                                                       'user_bus',
                                                       'id',
                                                       'cities',
                                                       'regin',)



    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in search_filer:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            # p = CreateBusiness(sel_city=tmp_s[1])
            # sel_city = p.get_sel_city_display()
            #
            # p = CreateBusiness(sel_distr=tmp_s[2])
            # sel_distr = p.get_sel_distr_display()

            # cities_name_b = AllCities.objects.filter(id=tmp_s[8]).values('name')
            # distr_name_b = AllCities.objects.filter(id=tmp_s[9]).values('name')
            # search_filer_pro = Profession.objects.filter(id=tmp_s[10]).values('name')
            # cities_b = p.get_cities_b_display()
            # print('search_filer_pro')
            # print(search_filer_pro[0]['name'])
            list_tmp = list(tmp_s)
            # list_tmp[1] = sel_city
            # list_tmp[2] = sel_distr
            # list_tmp[8] = cities_name_b[0]['name']
            # list_tmp[9] = distr_name_b[0]['name']
            # list_tmp[10] = search_filer_pro[0]['name']
            # list_tmp[11] = search_filer_pro[0]['name']
            # лайки
            user_like = LikeBusinesModel.objects.filter(first_id=tmp_s[4]).filter(second_id=request.user.id).values_list('id')
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s

            # AllCities.cities_b.all()
        tmp_categ_name.append(tmp_categ_name_list)# формируем массив со всеми анкетами


    return render(request, 'all_busines.html', {'serxh_filer': tmp_categ_name, 'allCities': allCities, 'form': form, 'distinr': distinr})


def likes(request):
    # likes заносим в таблицу лайкующего и хозяйна анкеты
    test_user = User.objects.filter(id=request.POST.get('first')).values('username', 'email')
    nearly_final = LikeModel(like_first=test_user[0]['username'], email_first=test_user[0]['email'],
                             like_second=request.POST.get('second'), email_second=request.POST.get('email'),
                             first_id=request.POST.get('first'), second_id=request.POST.get('second_id'),
                             id_ancket=request.POST.get('id_ancket'),)
    nearly_final.save(force_insert=True)
    return redirect('/all_neighb/')

def likes_busines(request):
    # likes заносим в таблицу лайкующего и хозяйна анкеты
    test_user = User.objects.filter(id=request.POST.get('first')).values('username', 'email')
    nearly_final = LikeBusinesModel(like_first=test_user[0]['username'], email_first=test_user[0]['email'],
                                    like_second=request.POST.get('second'), email_second=request.POST.get('email'),
                                    first_id=request.POST.get('first'), second_id=request.POST.get('second_id'),
                                    id_ancket=request.POST.get('id_ancket'),)
    nearly_final.save(force_insert=True)
    return redirect('/all_busines/')

def statistics(request):
    # статистика

    count_us = User.objects.values('username', 'email')


    count_users = (len(count_us))
    all_likes = LikeModel.objects.values()
    count_stat = len(all_likes)/2
    all_likes_n = math.ceil(count_stat)
    all_likes_b = LikeBusinesModel.objects.values()
    count_stat = len(all_likes_b)/2
    all_likes_bus = math.ceil(count_stat)
    # for count_us_s in count_us:
    print(count_us[0]['username'])
    tmp =count_us[0]['username']
    all_likes_count = LikeModel.objects.filter(like_second=count_us[0]['username']).count()
    all_likes_count_two = LikeModel.objects.filter(like_first=count_us[0]['username']).count()

    if all_likes_count > 0 and all_likes_count_two > 0:
        # print('tmp')
        # print(tmp)
        all_likes_count_two_two = LikeModel.objects.filter(like_first=count_us[0]['username']).values()
        # print('all_likes_count_two_two ')
        # print(all_likes_count_two_two[0]['like_first'])
        # save_end_like = LikeEndModelNe(like_first=all_likes_count_two_two[0]['like_first'],
        #                                email_first=all_likes_count_two_two[0]['email_first'],
        #                                like_second=all_likes_count_two_two[0]['like_second'],
        #                                email_second=all_likes_count_two_two[0]['email_second'],)
        # print('save_end_like')
        # print(save_end_like)
        # save_end_like.save()
        # print(all_likes_count, all_likes_count_two)



    return render(request, 'statistics.html', {'count_users':count_users, 'all_likes_n': all_likes_n, 'all_likes_bus': all_likes_bus})

def tree_form(request):
    # по айди города получаем районы
    dict1 = {}
    # print(request.GET.get('id'))
    city_id = request.GET.get('id')
    all_child = AllCities.objects.filter(parent_id=city_id).values('name', 'id')
    # print('all_child')
    # print(all_child)
    dict1['data']=list(all_child)# словарь в словаре для передачи json
    # print('dict1')
    # print(dict1)
    return JsonResponse(dict1)

def tree_form_b(request):
    dict2 = {}
    print(request.GET.get('id'))
    city_id = request.GET.get('id')
    all_child = AllCities.objects.filter(parent_id=city_id).values('name', 'id')
    print('all_child_b-450')
    print(all_child)
    # return HttpResponse('1')

    dict2['data']=list(all_child)
    print('dict1_b-456')
    print(dict2)
    # return JsonResponse({'all_child': all_child, 'status': 'ok', 'dict1': dict1})
    return JsonResponse(dict2)
    # return HttpResponse({'all_child': all_child,})

def search_fetch(request):
    # по айди города, района и пол соседа получаем анкты
    print('distr-461')
    print(request.GET.get('id'))

    print('seacrprof464')
    print(request.GET.get('distr'))
    print(request.GET)
    cities_name = AllCities.objects.filter(id=request.GET.get('id')).values('name')
    distr_name = AllCities.objects.filter(id=request.GET.get('distr')).values('name')
    catalog_filter=CreateNeighbour.objects.filter(cities=cities_name[0]['name'],
                                                  regin=distr_name[0]['name'],
                                                  gender=request.GET.get('ender')).\
                                                                values_list('id',
                                                                             'name',
                                                                             'gender',
                                                                             'gender_neighb',
                                                                             # 'sel_city',
                                                                             # 'sel_distr',
                                                                             'presence_animals',
                                                                             'presence_flat',
                                                                             'attitude_animals',
                                                                             'attitude_smok',
                                                                             'about_me',
                                                                             'image',
                                                                             'user_neig',
                                                                             'cities',
                                                                             'regin',)
    print('catalog_filter')
    print(catalog_filter)
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    # формируем масив лдя прорисовки в шблоне
    for all_goods_s in catalog_filter:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateNeighbour(gender=tmp_s[2])
            gender = p.get_gender_display()

            p = CreateNeighbour(gender_neighb=tmp_s[3])
            gender_neighb = p.get_gender_neighb_display()

            # p = CreateNeighbour(sel_city=tmp_s[4])
            # sel_city = p.get_sel_city_display()
            #
            # p = CreateNeighbour(sel_distr=tmp_s[5])
            # sel_distr = p.get_sel_distr_display()

            p = CreateNeighbour(attitude_animals=tmp_s[4])
            attitude_animals = p.get_attitude_animals_display()

            p = CreateNeighbour(attitude_smok=tmp_s[5])
            attitude_smok = p.get_attitude_smok_display()

            # cities_name = AllCities.objects.filter(id=tmp_s[11]).values('name')
            # distr_name = AllCities.objects.filter(id=tmp_s[12]).values('name')

            list_tmp = list(tmp_s)
            list_tmp[2] = gender
            list_tmp[3] = gender_neighb
            # list_tmp[4] = sel_city
            # list_tmp[5] = sel_distr
            list_tmp[4] = attitude_animals
            list_tmp[5] = attitude_smok

            list_tmp[11] = cities_name[0]['name']
            list_tmp[12] = distr_name[0]['name']
            user_like = LikeModel.objects.filter(first_id=tmp_s[10]).filter(second_id=request.user.id).values_list('id') # лайки в шаблоне
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)

            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list) # формируем массив со всеми анкетами
        print('allCities')
        print(tmp_categ_name)
    return render(request, 'filtr_neig.html', {'filter_ne':tmp_categ_name})
    # return JsonResponse(dict1)

def search_fetch_b(request):
    # dict1 = {}

    # filter_ne= CreateNeighbour.objects.filter(cities_id=request.GET.get('id')).values()
    # print('filter_ne')
    # print(filter_ne)
    print('distr-513')
    print(request.GET.get('id'))

    print('seacrprof546')
    print(request.GET.get('distr'))
    print('seacrprof-548')
    print(request.GET.get('prof'))
    # dict1['data']=list(filter_ne)
    allCities = AllCities.objects.all()
    # catalog_filter = CreateNeighbour.objects. \
    # catalog_filter=CreateNeighbour.objects.filter(cities_id=request.GET.get('id'),districts_tree=request.GET.get('distr'),gender=request.GET.get('ender')). \, category_bus=request.GET.get('prof'))\
    cities_name = AllCities.objects.filter(id=request.GET.get('id')).values('name')
    distr_name = AllCities.objects.filter(id=request.GET.get('distr')).values('name')
    search_filer = CreateBusiness.objects.filter(cities=cities_name[0]['name'],
                                                 regin=distr_name[0]['name'],
                                                 category_bus=request.GET.get('prof')).values_list('name_bus',
                                                                                                     # 'sel_city',
                                                                                                     # 'sel_distr',
                                                                                                     'category_bus',
                                                                                                     'about_me',
                                                                                                     'image',
                                                                                                     'user_bus',
                                                                                                     'id',
                                                                                                     'cities',
                                                                                                     'regin',)

    print('search_filer-561')
    print(search_filer)
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in search_filer:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            # p = CreateBusiness(sel_city=tmp_s[1])
            # sel_city = p.get_sel_city_display()
            #
            # p = CreateBusiness(sel_distr=tmp_s[2])
            # sel_distr = p.get_sel_distr_display()

            list_tmp = list(tmp_s)
            # list_tmp[1] = sel_city
            # list_tmp[2] = sel_distr
            user_like = LikeBusinesModel.objects.filter(first_id=tmp_s[4]).filter(second_id=request.user.id).values_list('id')
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list)# формируем массив со всеми анкетами
        print('tmp_categ_name-598')
        print(tmp_categ_name)
    return render(request, 'test_busines.html', {'serxh_filer': tmp_categ_name})
    # return JsonResponse(dict1)
