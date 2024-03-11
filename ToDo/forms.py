from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

