import django.forms as f
from django.forms import modelformset_factory

from travel.models import Post, Photo


class PhotoForm(f.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo_path', 'description']


class PostForm(f.ModelForm):
    title = f.CharField(max_length=30)
    content = f.CharField(max_length=5000, label="Content:", widget=f.Textarea(attrs={'placeholder': 'What do you want to share with us?'}))

    class Meta:
        model = Post
        fields = ['title', 'city', 'country', 'content', 'category']













