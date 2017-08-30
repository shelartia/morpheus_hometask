from django.forms import ModelForm
from .models import Comments, Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        #fields = '__all__'
