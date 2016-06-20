from django.db import models
from django.utils import timezone


# News Table
class Lady(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name='Content')
    date = models.DateField(default=timezone.now, verbose_name='Date')
    pictures = models.ImageField(upload_to='Ladies/%Y/%m/%d/', verbose_name="Pictures")
    reference_link = models.URLField(verbose_name='Reference URL')
    type_id = models.ForeignKey('LadyType')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ladies'
        verbose_name_plural = 'Ladies'

# News Type Table
class LadyType(models.Model):
    LanguageID = models.ForeignKey('Language.language', verbose_name="Language")
    type = models.CharField(max_length=255, verbose_name='Tool Types')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'LadyType'
        verbose_name_plural = 'LadyType'

