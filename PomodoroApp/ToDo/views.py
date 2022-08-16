from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList


def todo_page(request):
    todo_list = ToDoList.objects.all().order_by('-dead_line')
    return render(request, 'ToDo/todopage.html', locals())



def item_delete (request, pk):
    todo_item = get_object_or_404 (ToDoList, pk=pk)
    if request.method == 'POST':         # If method is POST,
        todo_item.delete()                     # delete the cat.
        return redirect('/todo/')             # Finally, redirect to the homepage.

    return render(request, 'ToDo/todopage.html', {'todo_item':todo_item})
