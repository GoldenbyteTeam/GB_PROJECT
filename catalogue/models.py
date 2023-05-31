from django.db import models


# Create your models here.

class Keywords(models.Model):
    """
    Example of Json_keyword
    {"color": "#008080", "keywords": ["aggr"]}
    """
    name = models.CharField(max_length=100)
    keywords = models.JSONField(null=True)
    class Meta:                             #fix plural name in django administration
        verbose_name_plural = "keywords"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,null=False,default="Others")
    not_empty = models.BooleanField(default=True)
    class Meta:                             #fix plural name in django administration
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Catalogue(models.Model):
    title = models.CharField(max_length=100,null=False)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null="False")
    keywords = models.ForeignKey(Keywords,on_delete=models.DO_NOTHING,null="True",blank="True")
    default_hostname = models.CharField(max_length=100, null="True",blank="True")
    image_catalogue = models.ImageField(null=False)
    is_published = models.BooleanField(default=True)



    def __str__(self):
        return self.title

