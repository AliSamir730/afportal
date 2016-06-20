from django.db import models
from Language.models import language


class CountryList(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    Title = models.CharField(max_length=255, verbose_name="Title")

    def __str__(self):
        return self.Title


class CityList(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    CountryID = models.ForeignKey('CountryList', verbose_name="Country")
    Title = models.CharField(max_length=255, verbose_name="Title")

    def __str__(self):
        return self.Title


class DayList(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    CityID = models.ForeignKey('CityList', verbose_name="City")
    Day = models.CharField(max_length=255, verbose_name="Day")
    Values = models.CharField(max_length=255, verbose_name="Value")

    def __str__(self):
        return self.Title

# Create your models here.
