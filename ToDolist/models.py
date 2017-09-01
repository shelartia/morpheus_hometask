from datetime import datetime, date
import time

from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    finished_at = models.DateTimeField(default=datetime.now(), blank=True)
    finished = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    deadline = models.DateField(default=date.today(), blank=True)

    def __str__(self): #this is to return the name of the object.
        return self.title