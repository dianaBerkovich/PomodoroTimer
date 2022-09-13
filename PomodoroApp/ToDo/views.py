from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from .form import TodoForm
from django.template import loader
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

def delete_item(request, id):
    todo_item = ToDoList.objects.get (id = id)
    todo_item.delete()
    return redirect ('todo_page')


def update_item(request, id):
    todo_item = ToDoList.objects.get (id = id)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            todo_item.title = data.get ('title')
            todo_item.dead_line = data.get ('dead_line')
            todo_item.state = data.get ('state')
            todo_item.description = data.get('description')
            todo_item.save()
            return redirect ('todo_page')
    else:
            form = TodoForm()
            form.initial['title'] = todo_item.title
            form.initial['dead_line'] = todo_item.dead_line
            form.initial['state'] = todo_item.state
            form.initial['description'] = todo_item.description
            return render(request, 'ToDo/update.html', {'form': form})


def updaterecord_item (request, id):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get ('title')
            dead_line = data.get ('dead_line')
            state = data.get ('state')
            description = data.get('description')
            ToDoList.objects.save(title = title, dead_line = dead_line,state = state, description = description)
            return redirect ('todo_page')
    else:
        form = TodoForm()
        todo_list = ToDoList.objects.all().order_by('-dead_line')
        return render(request, 'ToDo/todopage.html', locals())



def delete_all (request):
    ToDoList.objects.all().delete()
    return redirect ('todo_page')

# def update(request, id):
#   mymember = Members.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))