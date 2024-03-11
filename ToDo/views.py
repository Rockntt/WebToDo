from django.shortcuts import render, redirect
from .models import ToDoTask
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    tasks = ToDoTask.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        existing_task = ToDoTask.objects.filter(title=title, user=request.user).exists()
        if not existing_task:
            task = ToDoTask(user=request.user, title=title, description=description)
            task.save()
            return redirect('')  # Перенаправляем на страницу со списком заданий

    return render(request, 'html/index.html', {'tasks': tasks})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # После успешной регистрации можно перенаправить пользователя на другую страницу
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'html/signup.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # После успешного входа пользователя можно перенаправить его на другую страницу
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'html/signin.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')
