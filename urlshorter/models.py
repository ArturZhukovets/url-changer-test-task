from django.db import models
from django.core.validators import MinLengthValidator


class Url(models.Model):
    source_url = models.CharField(max_length=500, validators=[MinLengthValidator(8)])
    url_id = models.CharField(max_length=20)

