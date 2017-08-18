from django.shortcuts import render, render_to_response
from django.contrib import auth
# Create your views here.


def tasks(request):
    #all_article = Article.objects.all() # Передаю в переменную все статьи
    #current_page = Paginator(all_article, 3) # Передача пагинатору всех статей и вывод 3 на страницу
    return render_to_response('task/task.html', {
        #'articles': Article.objects.all(), # Получаем все обьекты Статей
        #'articles': current_page.page(page_number),
        'username': auth.get_user(request).username, # Получаем юзера из реквеста
    })


def start(request):
    return render_to_response('todolist/main.html')