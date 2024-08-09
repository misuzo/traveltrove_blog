from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, help_text='Tell us something about yourself.')
    country = models.CharField(max_length=60, blank=True, help_text='Where are you from?')

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'users'


