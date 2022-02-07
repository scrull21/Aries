from django import forms 
from apps.users.models import User 
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username' 'email', 'profile_image'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'profile_image': forms.FileInput(attrs={'class': "form-control"}),
        }