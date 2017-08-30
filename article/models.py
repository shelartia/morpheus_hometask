from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Article(models.Model): # Статья
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'article'

    article_title = models.CharField(verbose_name='Название статьи', max_length=200)
    article_text = models.TextField(verbose_name='Текст статьи', max_length=800, null=True, blank=True)
    article_date = models.DateTimeField(verbose_name='Добавлена')
    article_likes = models.IntegerField(default=0, editable=False) # editable - скрывает поле в админке
    article_creator = models.ForeignKey(User)

    def __str__(self):
        return self.article_title


class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'

    comments_text = models.TextField(verbose_name='Комментарий', max_length=400)
    comments_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    comments_article = models.ForeignKey(Article)#, editable=False) # Связь с таблицей статей

