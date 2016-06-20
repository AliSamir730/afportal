from django.db import models
from Language.models import language

class TVList(models.Model):
    LanguageID = models.ForeignKey('Language.language',verbose_name="Language")
    Title = models.CharField(max_length=255,verbose_name="Title")
    Descriptions = models.TextField(verbose_name="Meta Descriptions")
    Keywords = models.CharField(max_length=255,verbose_name="Meta Keywords")
    Text = models.TextField(verbose_name="Text")
    def __str__(self):
        return self.Title

class TVProgramm(models.Model):
    LanguageID = models.ForeignKey('Language.language',verbose_name="Language")
    TVID = models.ForeignKey('TVList',verbose_name="TV name")
    Day = models.CharField(max_length=255,verbose_name="Title")
    Descriptions = models.TextField(verbose_name="Meta Descriptions")
    def __str__(self):
        return self.Day
# Create your models here.
