from django.db import models


class Gcam(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    config = models.CharField(max_length=100, default="0")
