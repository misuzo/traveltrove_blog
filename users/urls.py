"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from users import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='users-signup'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('login/', views.CustomLogInView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password-change')
]
