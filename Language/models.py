from django.db import models

class language(models.Model):
    title = models.CharField(max_length=255,verbose_name="Language")
    def __str__(self):
        return self.title

# Create your models here.
