from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^add_item/(?P<task_id>\d+)/$', views.add_item, name='add_item'),
    #url(r'^add_task/(\d+)/$', views.add_task, name='add_task'),
    url(r'^', views.tasks, name='all_tasks_user')
]