from django.shortcuts import render
from .models import ToDoTask

# Create your views here.

def home(request):
    tasks = ToDoTask.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ToDoTask.objects.create(title=title, description=description)

    return render(request, 'html/index.html', {'tasks': tasks})