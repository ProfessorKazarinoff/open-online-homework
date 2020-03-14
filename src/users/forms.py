# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = UserCreationForm.Meta.fields + ("id_number", "institution")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
