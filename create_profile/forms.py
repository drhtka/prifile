# -*- coding: utf-8 -*-
from django import forms
from create_profile.models import CreateNeighbour, CreateBusiness

class CreateForms(forms.ModelForm):
    # добавляем соседа
    class Meta:
        model = CreateNeighbour
        fields = ('name',
                  # 'user_neig',
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
                  'user_neig',)
                  # 'cities',
                  # 'districts_tree',)

    def __init__(self, *args, **kwargs):
        super(CreateForms, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Фамиля Имя Отчество'
        self.fields['about_me'].widget.attrs['placeholder'] = 'О себе'

class CreateFormsB(forms.ModelForm):
    # добавляем бизнес
    class Meta:
        model = CreateBusiness
        fields = ('name_bus',
                  # 'sel_city',
                  # 'sel_distr',
                  'category_bus',
                  'about_me',
                  'image',
                  'user_bus')

    def __init__(self, *args, **kwargs):
        super(CreateFormsB, self).__init__(*args, **kwargs)
        self.fields['name_bus'].widget.attrs['class'] = 'form-control'
        self.fields['name_bus'].widget.attrs['placeholder'] = 'Фамиля Имя Отчество'
        self.fields['category_bus'].widget.attrs['class'] = 'form-control'
        self.fields['category_bus'].widget.attrs['placeholder'] = 'Впишите категорию бизнеса'
        self.fields['category_bus'].widget.attrs['required'] = 'True'
        # self.fields['about_me'].widget.attrs['class'] = 'res_non'
        self.fields['about_me'].widget.attrs['placeholder'] = 'О себе'