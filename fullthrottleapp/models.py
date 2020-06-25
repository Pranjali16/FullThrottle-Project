from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser, models.Model):
    """User Model"""
    name = models.CharField(max_length=500, blank=True, null=True)
    tz = models.CharField(max_length=500, blank=True, null=True)

    USERNAME_FIELD = 'name'

    def __str__(self):
        return str(self.name)


class ActivityPeriod(models.Model):
    """ Activity Period Model"""
    user_id = models.ForeignKey(User, related_name='user_activity', null=True, blank=True,
                                on_delete=models.CASCADE)
    start_time = models.CharField(max_length=500, blank=True, null=True)
    end_time = models.CharField(max_length=500, blank=True, null=True)
