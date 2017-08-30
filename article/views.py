from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth


# Create your views here.


def template_one(request):
    view = "Article title"
    return render_to_response('article/article_view.html', {'name': view})


def articles(request, page_number=1):
    all_article = Article.objects.all() # Передаю в переменную все статьи
    current_page = Paginator(all_article, 3) # Передача пагинатору всех статей и вывод 3 на страницу
    return render_to_response('article/articles.html', {
        #'article': Article.objects.all(), # Получаем все обьекты Статей
        'articles': current_page.page(page_number),
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


def article(request, article_id=1):
    article = get_object_or_404(Article, id=article_id)
    comments = Comments.objects.all()
    form_comments = CommentForm
    context = {
        'article': Article.objects.get(id=article_id),
        'comments': Comments.objects.filter(comments_article_id=article_id),
        'form_comments': form_comments,
        'username': auth.get_user(request).username,
    }

    template = 'article/article.html'
    return render(request, template, context)


def add_like(request, article_id):
    try:
        if article_id in request.COOKIES: # Проверка кукифайлов и редирект на ту же страницу
            redirect('/article/all')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1 # Накрутка счетчика лайков
            article.save()
            responce = redirect('/article/all')
            responce.set_cookie(article_id, 'test') # Передаем данные в куки
            return responce
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/article/all')


def add_comment(request, article_id):
    if request.POST and ('pause' not in request.session):
        # Проверка что данные передаються методом Post и дополннительно ограничиваем время сессии
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(10) # Создает сессию и хранит ее 0 мин. 10 сек.
            request.session['pause'] = True # Пауза сессии
    return redirect('/article/get/%s' % article_id)
