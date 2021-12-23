# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey


class AllCities(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Город Район'
        verbose_name_plural = 'Районы'
        db_table = 'districts'

class CreateNeighbour(models.Model):
    # Добавить соседа

    class Meta:
        verbose_name = 'Сосед'
        verbose_name_plural = 'Анкеты соседи'
        db_table = 'neighbour_rec'
        ordering = ['-id']

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    # cities = TreeForeignKey(AllCities, on_delete=models.PROTECT, default=0, verbose_name='Город', related_name='cities')
    # districts_tree = TreeForeignKey(AllCities, on_delete=models.PROTECT, default=1, verbose_name='Район', related_name='districts_tree')
    #tags = GenericRelation(District)
    user_neig = models.ForeignKey(
        # User,auth.User
        'auth.User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        # auto_created=True,
        blank=True,
        null=True,)
        # editable=False,
        # default='auth.User'

    name = models.CharField('ФИО', max_length=100, blank=False, unique=True)

    man = '1'
    woman = '2'
    GENDER_CHOICES = (
        (man, 'Мужчина'),
        (woman, 'Женщина'),

    )
    gender = models.CharField('Выбрать пол', max_length=15, choices=GENDER_CHOICES, blank=False)

    man = '1'
    woman = '2'
    never_mind = '3'
    GENDER_CHOICES_NEIGHB = (
        (man, 'Мужчина'),
        (woman, 'Женщина'),
        (never_mind, 'Неважно'),
    )
    gender_neighb = models.CharField('Выбрать пол соседа', max_length=15, choices=GENDER_CHOICES_NEIGHB, blank=False)

    presence_animals = models.BooleanField('Наличие животных',)
    # presence_flat = models.CharField('Наличие квартиры', max_length=2, blank=True,)
    presence_flat =models.BooleanField('Наличие квартиры',)

    positive = '1'
    neutral = '2'
    negative = '3'
    ATTITUDE_ANOMALS = (
        (positive, 'положительное'),
        (neutral, 'нейтральное'),
        (negative, 'отрицательное'),

    )
    attitude_animals = models.CharField('Отношение к животным', max_length=15, choices=ATTITUDE_ANOMALS, blank=False)

    positive = '1'
    neutral = '2'
    negative = '3'

    ATTITUDE_SMOKING = (
        (positive, 'положительное'),
        (neutral, 'нейтральное'),
        (negative, 'отрицательное'),

    )

    attitude_smok = models.CharField('Отношение к курящему', max_length=15, choices=ATTITUDE_SMOKING, blank=False)
    about_me = models.TextField('О себе', max_length=255, blank=False)
    image = models.ImageField(upload_to='images_n',  blank=False, null=False, verbose_name='Загрузить изображение')
    cities = models.CharField('Город', max_length=100, blank=True)
    regin = models.CharField('Район', max_length=100, blank=True)

    def __str__(self):
        return self.name

class CreateBusiness(models.Model):
    # Добавить бизнес

    class Meta:
        verbose_name = 'Бизенс'
        verbose_name_plural = 'Анкеты бизнес'
        db_table = 'business'
        ordering = ['-id']

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    user_bus = models.ForeignKey(
        # User,
        'auth.User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        # auto_created=True,
        blank=True,
        null=True,)
    name_bus = models.CharField('ФИО', max_length=100, blank=False)

    category_bus = models.CharField('Категория бизнеса', max_length=100, blank=False,)
    about_me = models.TextField('Информация', max_length=255, blank=False)
    image = models.ImageField(upload_to='images_bus', blank=False, null=False, verbose_name='Загрузить изображение')
    cities = models.CharField('Город', max_length=100, blank=True)
    regin = models.CharField('Район', max_length=100, blank=True)
    def __str__(self):
        return self.name_bus


class LikeModel(models.Model):
    # Лайки

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки сожителей'
        db_table = 'like_model'

    like_first = models.CharField('Хозяин анкеты', max_length=100, blank=True)
    email_first = models.CharField('Почта хозяйна анкеты', max_length=100, blank=True)
    like_second = models.CharField('Авторизированный', max_length=100, blank=True)
    email_second = models.CharField('Почта авторизованного', max_length=100, blank=True)
    date_like = models.DateField('Дата создания', auto_now=True)
    first_id = models.CharField('ID Хозяинa анкеты', max_length=100, blank=True)
    second_id = models.CharField('ID Почта авторизованного', max_length=100, blank=True)
    id_ancket = models.CharField('ID анкеты', max_length=100, blank=True)
    def __str__(self):
        return self.like_first

class LikeBusinesModel(models.Model):
    # Лайки

    class Meta:
        verbose_name = 'лайк бизнес'
        verbose_name_plural = 'лайки бизнес'
        db_table = 'like_busines_model'

    like_first = models.CharField('лайк-1', max_length=100, blank=True)
    like_second = models.CharField('лайк-2', max_length=100, blank=True)
    date_like = models.DateField('Дата создания', auto_now=True)
    email_first = models.CharField('Почта хозяйна анкеты', max_length=100, blank=True)
    email_second = models.CharField('Почта авторизованного', max_length=100, blank=True)
    first_id = models.CharField('ID Хозяинa анкеты', max_length=100, blank=True)
    second_id = models.CharField('ID Почта авторизованного', max_length=100, blank=True)
    id_ancket = models.CharField('ID анкеты', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.like_first


