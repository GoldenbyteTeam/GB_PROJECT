from django.db import models

from catalogue.models import Catalogue

# Create your models here.

class Environment(models.Model):
    name = models.CharField(max_length=200,unique=True)
    catalogue = models.ForeignKey(Catalogue,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name