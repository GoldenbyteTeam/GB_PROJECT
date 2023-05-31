from django.db import models
from django.contrib.auth.models import User

from gb.settings import AVATAR_DIR,BASE_DIR

from os import path,listdir
from random import randint



def avocato_picker(base_dir,avatar_dir,media_dir='media'):
    """
    Avocatos NFTs: https://rarible.com/avocatos/owned
    """
    avocato_list = listdir(path.join((path.join(base_dir, media_dir)), avatar_dir))
    avocato_choice = randint(1, len(avocato_list))

    for avocato in avocato_list:
        if "{:02d}".format(avocato_choice) in avocato[:2]: # compare the number of avocato
            return path.join(avatar_dir, avocato)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    avatar = models.ImageField(default=avocato_picker(BASE_DIR,AVATAR_DIR),upload_to=AVATAR_DIR)
    jobtitle = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField()
    website_url = models.URLField(max_length=200,null=True,blank=True)
    facebook_url = models.URLField(max_length=200,null=True,blank=True)
    instagram_url = models.URLField(max_length=200,null=True,blank=True)
    linkedin_url = models.URLField(max_length=200,null=True,blank=True)
    is_published = models.BooleanField(default=True,name="Published",help_text="(add profile to contributors)")

    def __str__(self):
        return self.user.username
