from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()

class Category(models.Model):

    cat_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.cat_name


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=1)
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    country = CountryField()
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








