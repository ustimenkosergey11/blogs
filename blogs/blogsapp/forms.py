from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Post

User = get_user_model()


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name')


class AddPostForm(forms.ModelForm):
    title = forms.TextInput
    description = forms.Textarea
    author = forms.CharField
    img = forms.FileField

    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'img')
        widgets = {
            'photo': forms.ImageField
        }
