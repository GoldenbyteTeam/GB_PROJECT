from django.db import models
from environment.models import Environment

# Create your models here.

class Opmode(models.Model):
    name = models.CharField(max_length=200)
    environment = models.ForeignKey(Environment, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
