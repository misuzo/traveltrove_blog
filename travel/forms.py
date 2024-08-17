import django.forms as f
from travel.models import Post, Photo, Category


class PhotoForm(f.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo_path', 'description']


class PostForm(f.ModelForm):
    title = f.CharField(max_length=30)
    content = f.CharField(
        max_length=5000,
        label="Content:",
        widget=f.Textarea(attrs={'placeholder': 'What do you want to share with us?'})
    )
    category = f.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=f.CheckboxSelectMultiple,
        label="Categories"
    )

    class Meta:
        model = Post
        fields = ['title', 'city', 'country', 'content', 'category']













