from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from smart_selects.db_fields import ChainedForeignKey

from environment.models import Environment
from opmode.models import Opmode
from catalogue.models import Catalogue
from datetime import datetime

# Create your models here.

class Command(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    catalogue = models.ForeignKey(Catalogue,on_delete=models.DO_NOTHING)
    environment = ChainedForeignKey(Environment,
                                    chained_field="catalogue",
                                    chained_model_field="catalogue",
                                    show_all=False,
                                    auto_choose=True,
                                    sort=True,
                                    on_delete=models.DO_NOTHING)
    opmode = ChainedForeignKey(Opmode,
                                chained_field="environment",
                                chained_model_field="environment",
                                show_all=False,
                                auto_choose=True,
                                sort=True,
                                on_delete=models.DO_NOTHING)
    command = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    refurl_1 = models.URLField(max_length=200,blank=True)
    refurl_2 = models.URLField(max_length=200,blank=True)
    refurl_3 = models.URLField(max_length=200,blank=True)
    refurl_4 = models.URLField(max_length=200,blank=True)
    refurl_5 = models.URLField(max_length=200,blank=True)
    cmd_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.command


