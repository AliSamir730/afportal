from django.db import models
from Language.models import language


class CategoryCompany(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    Title = models.CharField(max_length=255, verbose_name="Title")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Company(models.Model):
    Language = models.ForeignKey('Language.language', verbose_name="Language")
    CategoryID = models.ForeignKey('CategoryCompany', verbose_name="Category")
    CompanyName = models.CharField(max_length=255, verbose_name="Company Name")
    company_description = models.TextField(verbose_name="Company Description")
    company_text = models.TextField(verbose_name="Company Text")
    company_site = models.CharField(max_length=255, verbose_name="Company Site")

    def __str__(self):
        return self.CompanyName

    class Meta:
        verbose_name = 'Company List'  # название приложения в ед.
        verbose_name_plural = 'Company List'  # название мн. числ.

# Create your models here.
