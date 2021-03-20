from django.contrib import admin
from create_profile.models import CreateNeighbour, CreateBusiness, LikeModel, LikeBusinesModel, MoscowModel, MoscowSelectModel

class CreateNeighbourAdmin(admin.ModelAdmin):
    list_display = ('user_neig', 'gender', 'id', 'sel_city', 'sel_distr')
    list_filter = ('id',)
    # raw_id_fields = ('user_neig',)/

class CreateBusinessAdmin(admin.ModelAdmin):
    list_display = ('name_bus', 'user_bus', 'category_bus', 'id')
    list_filter = ('id',)


class LikeModelAdmin(admin.ModelAdmin):
    list_display = ('like_first', 'like_second', 'date_like')
    list_filter = ('date_like',)

class LikeBusinesModelAdmin(admin.ModelAdmin):
    list_display = ('like_first', 'like_second', 'date_like')
    list_filter = ('date_like',)


admin.site.register(CreateNeighbour, CreateNeighbourAdmin)
admin.site.register(CreateBusiness, CreateBusinessAdmin)
admin.site.register(LikeModel, LikeModelAdmin)
admin.site.register(LikeBusinesModel, LikeBusinesModelAdmin)
admin.site.register(MoscowModel)
admin.site.register(MoscowSelectModel)