from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'

    task_title = models.CharField(verbose_name='Title', max_length=60)
    task_date = models.DateTimeField(verbose_name='Add', auto_created=True)
    task_update = models.DateTimeField(verbose_name='UpDating', auto_now_add=True)
    task_creator = models.ManyToManyField(User, auto_created=User.is_active)

    def __str__(self):
        return self.task_title


class Task_items(models.Model):
    class Meta:
        verbose_name = 'Task_Item'
        verbose_name_plural = 'Task_Items'
        db_table = 'task_items'

    item_text = models.TextField(verbose_name='Test for task', max_length=400)
    item_date = models.DateTimeField(auto_now_add=True, verbose_name='Date add')
    item_is_complited = models.BooleanField(default=False)
    item_task = models.ForeignKey(Task)

    def __str__(self):
        return self.item_text
