from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, help_text='Tell us something about yourself.')
    country = CountryField()
    avatar = models.ImageField(null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'users'


