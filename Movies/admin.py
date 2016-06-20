from django.contrib import admin
from Movies.models import Movie, MovieTypes


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'country', 'imdb_rating')
    search_fields = ('title', 'date')
    list_filter = ('title', 'country', 'type_id')


admin.site.register(Movie, MoviesAdmin)



class MovieTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)



admin.site.register(MovieTypes, MovieTypeAdmin)
