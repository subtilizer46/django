# Create your views here.
from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def delete_todo(request):
    if request.method == 'POST':
        title2 = request.POST['title2']
        todo_item = TodoItem.objects.get(title=title2)
        todo_item.delete()
    return redirect('todo_list')