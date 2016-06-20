from django.contrib import admin
from Weather.models import *

admin.site.register(CountryList)
admin.site.register(CityList)
admin.site.register(DayList)

# Register your models here.
