from django.db import models

# Create your models here.

class Explorer(models.Model):
    title = models.CharField(max_length=100,null=False)
    awesome_font_logo = models.CharField(max_length=100,null=False)
    url = models.CharField(max_length=8000,null=False)

    def __str__(self):
        return self.title