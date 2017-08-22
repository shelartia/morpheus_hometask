from django.forms import ModelForm
from .models import Task, Task_items


class TaskForm(ModelForm):
    class Meta:
        model = Task_items
        fields = ['item_text']
        #fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_title']