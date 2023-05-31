from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile
from clicommands.models import Command


@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(,sender=User)
# def move_cmd_ownership(instance):
#
#     user_cmds = Command.objects.all().order_by('cmd_date').filter(owner_id=instance.id)
#     for cmd in user_cmds:
#         cmd.owner=instance
