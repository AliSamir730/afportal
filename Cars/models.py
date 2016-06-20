# Create your models here.

from django.db import models
from django.utils import timezone


# News Table
class Car(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    car_name = models.CharField(max_length=255, verbose_name="Car Name")
    description = models.TextField(verbose_name="Description")
    date = models.DateField(default=timezone.now, verbose_name="Date")
    pictures = models.ImageField(upload_to='Cars/%Y/%m/%d/', verbose_name="Car Pictures")
    reference_link = models.URLField(verbose_name="Source URL")
    type_id = models.ForeignKey('CarsType', verbose_name="Type")

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'


# News Type Table
class CarsType(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    type = models.CharField(max_length=255, verbose_name='Types')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'CarTypes'
        verbose_name_plural = 'CarTypes'
