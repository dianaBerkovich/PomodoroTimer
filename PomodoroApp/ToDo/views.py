from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from .form import TodoForm
from django.views   import View


def todo_page(request):
    if request.method == "GET":
        form = TodoForm()
        todo_list = ToDoList.objects.all().order_by('-dead_line')
        return render(request, 'ToDo/todopage.html', locals())
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get ('title')
            dead_line = data.get ('dead_line')
            state = data.get ('state')
            description = data.get('description')
            ToDoList.objects.create(title = title, dead_line = dead_line,state = state, description = description)
            return redirect ('todo_page')

    else:
        form = TodoForm()
        todo_list = ToDoList.objects.all().order_by('-dead_line')
        return render(request, 'ToDo/todopage.html', locals())



