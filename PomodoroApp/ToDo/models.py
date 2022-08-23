from django.db import models
from datetime import date
class ToDoList (models.Model):
    title = models.CharField (max_length=255)
    dead_line = models.DateField (default=date.today().strftime('%d-%m-%Y'))
    state = models.BooleanField (default=False)
    description = models.TextField (max_length=4096, blank=True, null=True)

    class Meta :
        verbose_name = "To do item"
        verbose_name_plural = "To do items"