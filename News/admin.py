from django.contrib import admin
from News.models import News
from News.models import NewsType


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'ref_link',)
    search_fields = ('title', 'date')
    list_filter = ('title', 'date', 'type_id')


admin.site.register(News, NewsAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)


admin.site.register(NewsType, TypeAdmin)
