from django.contrib import admin
from Ladies.models import Lady
from Ladies.models import LadyType


class LadiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'reference_link',)
    search_fields = ('title', 'date')
    list_filter = ('title', 'date')

admin.site.register(Lady, LadiesAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)


admin.site.register(LadyType, TypeAdmin)
