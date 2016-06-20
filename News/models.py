from django.db import models
from django.utils import timezone


# News Table
class News(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Contents")
    date = models.DateField(default=timezone.now, verbose_name="Date Published")
    pics = models.ImageField(upload_to='News/%Y/%m/%d/', verbose_name="News Pictures")
    ref_link = models.URLField(verbose_name="URL Reference")
    type_id = models.ForeignKey('NewsType', verbose_name="Types")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


# News Type Table
class NewsType(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    type = models.CharField(max_length=255, verbose_name="Types")

    def __str__(self):
        return self.type
