from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.utils import timezone

class CityModel(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        db_table = 'city_db'

    name = models.CharField('Город', max_length=100, blank=True)
    # tags = GenericRelation(District)
# return u"{0}, {1}".format(self.city, self.name)
    def __str__(self):
        return self.name
#
class DistrictsModel(models.Model):
    class Meta:
        verbose_name = 'Район москвы'
        verbose_name_plural = 'Районы Москвы'
        db_table = 'distr_db'

    cities = models.OneToOneField(CityModel, on_delete=models.CASCADE, null=True, default=1)
    kirovsky = '1'
    leninskiy = '2'
    october = '3'
    sverdlovsk = '4'
    soviet = '5'
    central = '6'
    railway = '7'
    SELECT_DISTRICT = (

        (kirovsky, 'Кировский'),
        (leninskiy, 'Ленинский'),
        (october, 'Октябрьский'),
        (sverdlovsk, 'Свердловский'),
        (soviet, 'Советский'),
        (central, 'Центральный'),
        (railway, 'Железнодорожный'),
    )

    sel_distr = models.CharField('Район', max_length=15, choices=SELECT_DISTRICT, blank=True)

    def __str__(self):
        return u"{0}".format(self.cities)

# class DistrictsModel(models.Model):
#     class Meta:
#         verbose_name = 'Район москвы'
#         verbose_name_plural = 'Районы Москвы'
#         db_table = 'distr_db'
#
#     cities = models.OneToOneField(CityModel, on_delete=models.CASCADE)
#     kirovsky = '1'
#     leninskiy = '2'
#     october = '3'
#     sverdlovsk = '4'
#     soviet = '5'
#     central = '6'
#     railway = '7'
#     SELECT_DISTRICT = (
#
#         (kirovsky, 'Кировский'),
#         (leninskiy, 'Ленинский'),
#         (october, 'Октябрьский'),
#         (sverdlovsk, 'Свердловский'),
#         (soviet, 'Советский'),
#         (central, 'Центральный'),
#         (railway, 'Железнодорожный'),
#     )
#
#     sel_distr = models.CharField('Район', max_length=15, choices=SELECT_DISTRICT, blank=True)
#
#     def __str__(self):
#         return u"{0}".format(self.cities)

# from django.db import models


class Rubric(MPTTModel):
    class Meta:
        verbose_name = 'Город дерево'
        verbose_name_plural = 'Города дерево'

    name = models.CharField(verbose_name='Район', max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name='Город', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=100, unique=False, blank=True, null=True)
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Article(models.Model):
    name = models.CharField(max_length=50)
    caregory = TreeForeignKey(Rubric, on_delete=models.PROTECT, default=0, verbose_name='Город', related_name='cities')
    # caregory_distr = TreeForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Район', related_name='districts_tree')
    text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name