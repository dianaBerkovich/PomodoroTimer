from django.contrib import admin
from .models import ToDoList

@admin.register(ToDoList )
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["title", "dead_line", "state" ]
    list_editable = ["state"]
    search_fields = ["title"]
    list_filter = ["dead_line","state"]