from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import CharField


class Url(models.Model):
    source_url = models.CharField(max_length=500, validators=[MinLengthValidator(8)])
    url_id = models.CharField(max_length=20)

    def __str__(self):
        return self.source_url

    class Meta:
        ordering = ['-id']





# Create your models here.
