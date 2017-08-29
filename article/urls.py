from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^/', views.template_one),  # 'article.views.template_one'),  # ссылка на ф-цию в представлении
    url(r'^all/$', views.articles, name='articles_all'), # Все статьи
    url(r'^get/(?P<article_id>\d+)/$', views.article),  # Статья по переходу
    url(r'^add_like/(?P<article_id>\d+)/$', views.add_like),
    url(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment),
    url(r'^page/(\d+)/$', views.articles, name='page'),
]
