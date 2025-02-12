from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Todo


def index(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {'todos': todo})

def addTodo(request):
    context = {}
    if request.method == 'GET':
        return redirect('/')
    else:
        title = request.POST.get('title')
        newTodo = Todo(title=title, completed=False)

        newTodo.save()
        return redirect('/')
def updateTodo(request, id):
    todo = get_object_or_404(Todo, id = id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('/')

def deleteTodo(request, id):
    todo = get_object_or_404(Todo, id = id)
    todo.delete()
    return redirect('/')
