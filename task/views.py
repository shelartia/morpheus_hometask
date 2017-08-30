from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib import auth
from task.models import Task, Task_items
from .forms import TaskForm, ItemForm
from django.template.context_processors import csrf
from django.template import RequestContext
# Create your views here.


def start(request):
    return render_to_response('todolist/base.html', {'username': auth.get_user(request).username})


def tasks(request):
    username = auth.get_user(request)
    all_user_tasks = Task.objects.filter(task_creator__username=username)
    for task_id in all_user_tasks:
        task_items = Task_items.objects.filter(item_task_id=task_id)

    return render(request, 'task/task.html', {
            'tasks': all_user_tasks,
            'username': auth.get_user(request).username, # Получаем юзера из реквеста
            'items': task_items,
        })


def task(request, task_id=None):
    task = get_object_or_404(Task, id=task_id)
    tasks = Task_items.objects.all()
    form_item = TaskForm

    context = {
        'article': Task.objects.get(id=task_id),
        'items': Task_items.objects.filter(items_task_id=task_id),
        'form_task': form_item,
        'username': auth.get_user(request).username,
    }

    template = 'task/task.html'

    return render(request, template, context)


def add_task(request, task_id):
    if request.POST: # and ("pause" not in request.session):
        form = TaskForm(request.POST)
        print('form:',form)
        if form.is_valid():
            args = {}
            print('args', args)
            args.update(csrf(request))
            task = form.save(commit=False)
            task.comments_article = Task.objects.get(id=task_id)
            form.save()
            #request.session.set_expiry(30)
            #request.session['pause'] = True
    return redirect('/task/%s/' % task_id, args)


def add_item(request, task_id):
    username = auth.get_user(request)
    print('request', request, 'item', task_id)
    if request.POST and ("pause" not in request.session):
        form = ItemForm(request.POST)

        if form.is_valid():
            args = {}
            args.update(csrf(request))
            item = form.save(commit=False)
            print(item)
            item.item_task = Task.objects.get(id=task_id)
            form.save()
            request.session.set_expiry(3) # time pause
            request.session['pause'] = True
            args['form'] = form
            args['username'] = username
    #return redirect('/task/item/%s/' % task_id)
    return render_to_response('task/task.html', args)
