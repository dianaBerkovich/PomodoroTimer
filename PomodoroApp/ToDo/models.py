from django.db import models

class ToDoList (models.Model):
    title = models.CharField (max_length=255)
    dead_line = models.DateField ()
    state = models.BooleanField (default=False)
    description = models.TextField (max_length=4096, blank=True, null=True)

    class Meta :
        verbose_name = "To do item"
        verbose_name_plural = "To do items"