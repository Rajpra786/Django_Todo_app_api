from django.db import models
from datetime import date

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=150)
    description = models.TextField()
    # date = models.DateField(_("Date"), default=date.today)
    date = models.DateField(("Date"), auto_now_add=True)
