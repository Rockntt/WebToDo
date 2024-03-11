from django.shortcuts import render
from .models import ToDoTask

# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        existing_task = ToDoTask.objects.filter(title=title, user=request.user).exists()
        if not existing_task:
            task = ToDoTask(user=request.user, title=title, description=description)
            task.save()
            return redirect('task_list')  # Перенаправляем на страницу со списком заданий

    return render(request, 'html/index.html', {'tasks': tasks})