from django.db import models
from users.models import User


import users.models


class Category(models.Model):

    CATEGORY_CHOICES = [
        ('solo', 'Travelling solo'),
        ('friends', 'Travelling with friends'),
        ('family', 'Travelling with family')
    ]

    cat_name = models.CharField(max_length=30, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_cat_name_display()


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='post_photos', on_delete=models.CASCADE)
    photo_path = models.ImageField(upload_to='photos/%d/%m/%Y')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Photo for {self.post.title}'








