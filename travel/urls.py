from django.contrib import admin
from django.urls import path, include
from travel import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about_view, name='about'),
    path('post/all', views.AllPostsView.as_view(), name='all-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-details'),
    path('post/new', views.add_post, name='add_post'),
    path('post/<int:pk>/update', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/confirm-delete/', views.confirm_delete, name='confirm-delete'),
    path('posts/my-posts/', views.my_posts, name='my-posts'),
    path('post/category/<str:cat_name>/', views.posts_by_category, name='post-category'),
    path('contact/', views.contact, name='contact')
]