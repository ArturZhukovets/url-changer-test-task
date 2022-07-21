from django.db import models



class FakeUserAgent(models.Model):
    full_ua = models.CharField(max_length=500, blank=False, unique=True)

