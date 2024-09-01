import django.forms as f
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_countries.fields import CountryField
import users


class SignUpForm(UserCreationForm):

    username = f.CharField(
        max_length=35,
        min_length=5,
        required=True,
        widget=f.TextInput(attrs={'title': 'Required. 5-25 characters. Letters, digits and @/./+/-/_ only.',
                                  'placeholder': 'Choose your username',
                           'class': 'form-control'
                                  }))

    email = f.CharField(
        required=True,
        widget=f.TextInput(attrs={'placeholder': 'Your e-mail'
                                  }))

    first_name = f.CharField(
        widget=f.TextInput(attrs={'placeholder': 'What\'s your name?'
                                  }))

    bio = f.CharField(
        max_length=200,
        required=False,
        widget=f.Textarea(attrs={'placeholder': 'Tell us something about yourself',
                                 'class': 'form-control'
                                 }))

    country = CountryField().formfield()

    password1 = f.CharField(
        label='Password',
        widget=f.PasswordInput(attrs={'title': 'Enter a strong password',
                                      'class': 'form-control',
                                      'data-toggle': 'password',
                                      'id': 'password'
                                      }))

    password2 = f.CharField(
        label='Confirm Password',
        widget=f.PasswordInput(attrs={'title': 'Re-enter your password for confirmation.',
                                      'class': 'form-control',
                                      'data-toggle': 'password',
                                      'id': 'password'
                                      }))

    avatar = f.ImageField(widget=f.FileInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'bio', 'country', 'password1', 'password2', 'avatar']


class LogInForm(AuthenticationForm):

    username = f.CharField(
        max_length=35,
        min_length=5,
        required=True,
        widget=f.TextInput(attrs={'title': 'Required. 5-25 characters. Letters, digits and @/./+/-/_ only.'})
    )

    password = f.CharField(
        label='Password',
        required=True,
        widget=f.PasswordInput(attrs={'title': 'Enter a strong password'}),
    )

    remember_me = f.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(f.ModelForm):

    username = f.CharField(
        max_length=35,
        min_length=5,
        required=True,
        widget=f.TextInput(attrs={'title': 'Required. 5-25 characters. Letters, digits and @/./+/-/_ only.',
                           'class': 'form-control'
                                  }))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(f.ModelForm):

    avatar = f.ImageField(widget=f.FileInput)

    bio = f.CharField(
        max_length=200,
        required=False,
        widget=f.Textarea(attrs={'placeholder': 'Tell us something about yourself.',
                                 'class': 'form-control'
                                 }))


    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'country']
