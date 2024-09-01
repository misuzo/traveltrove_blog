from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from config import settings
from travel.models import Post, Photo, Category
from travel.forms import PostForm, PhotoForm, ContactForm
from django.core.mail import send_mail


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')[:3]


def about_view(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'posts': latest_posts
    }
    return render(request, 'about.html', context=context)



class AllPostsView(ListView):
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


def posts_by_category(request, cat_name):

    if cat_name == 'no-category':
        category = None
        posts = Post.objects.filter(category__isnull=True).order_by('-created_at')
    else:
        category = get_object_or_404(Category, cat_name__iexact=cat_name)
        posts = Post.objects.filter(category=category).order_by('-created_at')

    request.session['previous_url'] = request.get_full_path()

    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'categories.html', context=context)


# def contact(request):
#     return render(request, 'contact.html')
#
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            send_mail(
                f'From {name}, Subject: {subject}',
                f'Message: {message}.',
                email,
                [settings.ADMIN_EMAIL], # Go to settings.py and change ADMIN_EMAIL = 'YOUR EMAIL'
                fail_silently=False,
            )

            return redirect('success')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')


@login_required
def add_post(request):

    PhotoFormSet = modelformset_factory(Photo,
                                        form=PhotoForm,
                                        extra=3,
                                        max_num=3,
                                        validate_max=True)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        photo_formset = PhotoFormSet(request.POST, request.FILES, queryset=Photo.objects.none())

        if post_form.is_valid() and photo_formset.is_valid():

            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            post_form.save_m2m()

            for form in photo_formset.cleaned_data:

                if form and 'photo_path' in form:
                    photo_path = form['photo_path']
                    description = form.get('description', '')
                    photo = Photo(post=new_post, photo_path=photo_path, description=description)
                    photo.save()

            return redirect('post-details', pk=new_post.pk)

    else:
        post_form = PostForm()
        photo_formset = PhotoFormSet(queryset=Photo.objects.none())

    context = {
        'post_form': post_form,
        'photo_formset': photo_formset,
    }

    return render(request, 'add_post.html', context=context)



@login_required
def update_post(request, pk):

    post = get_object_or_404(Post, id=pk)
    PhotoFormSet = modelformset_factory(Photo,
                                        form=PhotoForm,
                                        extra=3,
                                        max_num=3,
                                        validate_max=True,
                                        can_delete=True)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        photo_formset = PhotoFormSet(request.POST, request.FILES, queryset=Photo.objects.filter(post=post))

        if post_form.is_valid() and photo_formset.is_valid():
            updated_post = post_form.save(commit=False)
            updated_post.author = request.user
            updated_post.save()
            post_form.save_m2m()

            for form in photo_formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    photo = form.save(commit=False)
                    photo.post = updated_post
                    photo.save()
                elif form.cleaned_data.get('DELETE', False):
                    if form.instance.pk:
                        form.instance.delete()

            return redirect(reverse('post-details', kwargs={'pk': updated_post.pk}))
    else:
        post_form = PostForm(instance=post)
        photo_formset = PhotoFormSet(queryset=Photo.objects.filter(post=post))

    context = {
        'post_form': post_form,
        'photo_formset': photo_formset,
    }

    return render(request, 'update_post.html', context=context)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()

        referer = request.META.get('HTTP_REFERER')
        if referer:
            return HttpResponseRedirect(referer)
        else:
            return redirect('home')

    context = {
        'post': post
    }

    return render(request, 'confirm_delete.html', context=context)

@login_required
def confirm_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        previous_url = request.session.get('previous_url', '/')
        return redirect(previous_url)

    context = {
        'post': post
    }

    return render(request, 'confirm_delete.html', context=context)


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')

    request.session['previous_url'] = request.get_full_path()

    context = {
        'posts': posts
    }
    return render(request, 'my_posts.html', context=context)
