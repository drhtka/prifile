# from django.db import models
#
# # Create your models here.
# from django.utils import timezone
#
# class City(models.Model):
#     class Meta:
#         verbose_name = 'Город'
#         verbose_name_plural = 'Города'
#         db_table = 'citiy'
#
#     name = models.CharField('Город', max_length=100, blank=True)
#     # tags = GenericRelation(District)
#
#     def __str__(self):
#         return self.name
# #
# class Districts(models.Model):
#     class Meta:
#         verbose_name = 'Район москвы'
#         verbose_name_plural = 'Районы Москвы'
#         db_table = 'districts'
#
#     # cities = models.OneToOneField(Cities, on_delete=models.CASCADE)
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
#     sel_distr = models.CharField('Выбрать район', max_length=15, choices=SELECT_DISTRICT, blank=True)
#
#     def __str__(self):
#         return self.sel_distr