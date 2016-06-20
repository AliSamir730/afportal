from django.contrib import admin
from Cars.models import Car
from Cars.models import CarsType


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'date', 'reference_link',)
    search_fields = ('car_name', 'date')
    list_filter = ('car_name', 'type_id', 'date')


admin.site.register(Car, CarAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)


admin.site.register(CarsType, TypeAdmin)
