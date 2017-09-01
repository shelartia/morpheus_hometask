from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.db.models import DateField, DateTimeField
from django.forms import SelectDateWidget, TextInput, Textarea, DateTimeInput

from ToDolist.models import Todo


class TodoForm(forms.ModelForm):

    tododate = forms.DateTimeField(widget=SelectDateWidget())

    class Meta:

        model = Todo
        fields = ["title", "content", "tododate"]

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Baslik',
            'id': 'title'})
        self.fields['content'].widget = Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Yapilacak'})


# class TodoListForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['title', 'text', 'deadline', 'finished', 'finished_at', 'priority', 'created_at']#'__all__'