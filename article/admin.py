from django.contrib import admin
from article.models import Article, Comments

# Register your models here.

class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2 # Добавляем в админку коммент


class ArticleAdmin(admin.ModelAdmin): # отображение статей для админки
    inlines = [ArticleInline]
    list_filter = ['article_date'] # ADD в админку для фильтрования


admin.site.register(Article, ArticleAdmin) # Регестрируем статьи в админку
