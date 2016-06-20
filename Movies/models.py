from django.db import models


# News Table
class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Movie Title')
    desc = models.TextField(verbose_name='Movie Description')
    pictures = models.ImageField(upload_to='Movies/%Y/%m/%d/', verbose_name='Movie Pictures')
    country = models.CharField(max_length=255, verbose_name='Origin Country')
    producer = models.CharField(max_length=255, verbose_name='Producer')
    scenario = models.TextField(verbose_name='Scenario')
    operator = models.CharField(max_length=255, verbose_name='Operator')
    composer = models.CharField(max_length=255, verbose_name='Composer')
    artists = models.TextField(verbose_name='Artists')
    editor = models.CharField(max_length=255, verbose_name='Editor')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Budget')
    allowed_age = models.IntegerField(verbose_name='Allowed Age')
    mpaa_rating = models.IntegerField(verbose_name='MPAA Rating')
    duration = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Duration")
    imdb_rating = models.IntegerField(verbose_name='IMDB Rating')
    release_date = models.DateField(verbose_name='Release Date')
    reference_link = models.URLField(verbose_name='Reference URL')
    type_id = models.ForeignKey('MovieTypes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'


# News Type Table
class MovieTypes(models.Model):
    type = models.CharField(max_length=255, verbose_name='Movie Types')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Movie Types'
        verbose_name_plural = 'Movie Types'
