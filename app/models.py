from datetime import date, time

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from userena.models import UserenaBaseProfile


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=50)
    notice_at = models.TimeField(default=time(18, 00))
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_profile(instance, **kwargs):
    if not kwargs['created']:
        return

    Profile.objects.create(user=instance, nickname=instance.username)


class Item(models.Model):
    user = models.ForeignKey(User, related_name='items')
    text = models.CharField(max_length=255)
    date = models.DateField(default=date.today())
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['id']

class ItemLike(models.Model):
    item = models.ForeignKey(Item, related_name='likes')
    user = models.ForeignKey(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        unique_together = ('item', 'user')


class ItemComment(models.Model):
    item = models.ForeignKey(Item, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
