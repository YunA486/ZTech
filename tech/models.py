from django.db import models

class Tech(models.Model):
    name = models.CharField(max_length=10)
    urls = models.URLField()
