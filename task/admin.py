from django.contrib import admin
from task.models import Task, Task_items

# Register your models here.

class TaskInline(admin.StackedInline):
    model = Task_items
    extra = 1


class Task_Admin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_filter = ['task_date'] # filter for admin


admin.site.register(Task, Task_Admin)