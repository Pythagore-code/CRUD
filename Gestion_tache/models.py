from django.db import models

# Create your models here.

class Tache_CRUD(models.Model):
    name = models.CharField(max_length=100)
    maindate = models.DateField()
    enddate = models.DateField()