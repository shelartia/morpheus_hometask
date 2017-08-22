#from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib import auth
from task.models import Task, Task_items
from .forms import TaskForm, ItemForm
from django.template.context_processors import csrf
# Create your views here.


def start(request):
    return render_to_response('todolist/main.html', {'username': auth.get_user(request).username})


def tasks(request):
    username = auth.get_user(request)
    all_user_tasks = Task.objects.filter(task_creator__username=username)
    return render_to_response('task/task.html', {
        'tasks': all_user_tasks,
        #'tasks': tasks.objects.all(), # Получаем все обьекты Статей
        #'tasks': current_page.page(page_number),
        'username': auth.get_user(request).username, # Получаем юзера из реквеста
    })

# def article(request, article_id=1):
#     comment_form = CommentForm
#     args = {}
#     args.update(csrf(request))  # Проверка данных
#     args['articles'] = Article.objects.get(id=article_id)
#     args['comments'] = Comments.objects.filter(comments_article=article_id)
#     args['form'] = comment_form
#     return render_to_response('articles/article/article.html', args)


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
    if request.POST and ("pause" not in request.session):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.comments_article = Task.objects.get(id=task_id)
            form.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/task/%s/' % task_id)


def add_item(request, task_id):
    if request.POST and ("pause" not in request.session):
        form = ItemForm(request.POST)
        if form.is_valid():
            args={}
            args.update(csrf(request))
            item = form.save(commit=False)
            item.item_task = Task.objects.get(id=task_id)
            form.save()
            request.session.set_expiry(3) # time pause
            request.session['pause'] = True
            args['form'] = form
    #return redirect('/task/item/%s/' % task_id)
    #return render_to_response('task/task.html', args)
    return render('/')

# def article(request, article_id=1):
#     comment_form = CommentForm
#     args = {}
#     args.update(csrf(request))  # Проверка данных
#     args['articles'] = Article.objects.get(id=article_id)
#     args['comments'] = Comments.objects.filter(comments_article=article_id)
#     args['form'] = comment_form
#     return render_to_response('articles/article/article.html', args)