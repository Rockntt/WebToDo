from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields


class ToDoTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoTask
        fields = ['title', 'description']
