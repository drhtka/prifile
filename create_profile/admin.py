from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from mptt.admin import DraggableMPTTAdmin

from create_profile.models import CreateNeighbour, CreateBusiness, LikeModel, LikeBusinesModel, AllCities#,# District, Cities#, City_Distr

class CreateNeighbourAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_neig', 'gender', 'id', 'cities', 'regin')
    list_filter = ('id',)
    list_editable = ('user_neig', 'cities', 'regin')
    # raw_id_fields = ('user_neig',)/

class CreateBusinessAdmin(admin.ModelAdmin):
    list_display = ('name_bus', 'user_bus', 'category_bus', 'id', 'cities', 'regin')
    list_filter = ('id',)
    list_editable = ('cities', 'regin')

class LikeModelAdmin(admin.ModelAdmin):
    list_display = ('like_first', 'email_first', 'like_second', 'email_second', 'date_like')
    list_editable = ('email_first', 'email_second')
    list_filter = ('date_like',)

class LikeBusinesModelAdmin(admin.ModelAdmin):
    list_display = ('like_first', 'email_first', 'like_second', 'email_second', 'date_like')
    list_editable = ('email_first', 'email_second')
    list_filter = ('date_like',)

admin.site.register(
    AllCities,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ('cities', 'sel_distr')
#     list_filter = ['cities']
# from main.models import Image, Product


# class DistrictInline(GenericTabularInline):
#     model = District
#     list_filter = ('object_id')
#
#
# class CitiesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id')
#     inlines = [
#         DistrictInline,
#     ]


admin.site.register(CreateNeighbour, CreateNeighbourAdmin)
admin.site.register(CreateBusiness, CreateBusinessAdmin)
admin.site.register(LikeModel, LikeModelAdmin)
admin.site.register(LikeBusinesModel, LikeBusinesModelAdmin)
#admin.site.register(Cities)
#admin.site.register(City_Distr)
#admin.site.register(District, DistrictAdmin)
# admin.site.register(AllCities)
# admin.site.register(MoscowSelectModel)


# moskva = '1'
# krasnoyarsk = '2'
# achinsk = '3'
# abakan = '4'
# divnogorsk = '5'
# sosnovoborsk = '6'
#
# SELECT_CITY = (
#     (moskva, 'Москва'),
#     (krasnoyarsk, 'Красноярск'),
#     (achinsk, 'Ачинск'),
#     (abakan, 'Абакан'),
#     (divnogorsk, 'Дивногорск'),
#     (sosnovoborsk, 'Сосновоборск'),
# )