from city_distr.models import DistrictsModel, CityModel, Rubric, Article#, City_Distr
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin



admin.site.register(
    Rubric,
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
class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('cities', 'sel_distr')
    list_filter = ['cities']

admin.site.register(CityModel)
admin.site.register(Article)
# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(DistrictsModel, DistrictsAdmin)

#admin.site.register(City_Distr), DistrictAdmin