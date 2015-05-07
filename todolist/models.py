import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=160)
    deadline = models.DateTimeField('Deadline')
    progress = models.DecimalField(max_digits=3, decimal_places=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def status(self):
        return progress == 100
