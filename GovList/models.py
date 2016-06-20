from django.db import models
from Language.models import language

class CategoryGov(models.Model):
    LanguageID = models.ForeignKey('Language.language',verbose_name="Language")
    Title = models.CharField(max_length=255,verbose_name="Title")
    def __str__(self):
        return self.Title

class GOV(models.Model):
    Language = models.ForeignKey('Language.language',verbose_name="Language")
    CategoryID = models.ForeignKey('CategoryGov',verbose_name="Category")
    Title = models.CharField(max_length=255,verbose_name="Title")
    URL = models.CharField(max_length=255,verbose_name="URL")
    Views = models.CharField(max_length=255,verbose_name="Views")
    Descriptions = models.TextField(verbose_name="Descriptions")
    Text = models.TextField(verbose_name="Text")
    def __str__(self):
        return self.Title



# Create your models here.
