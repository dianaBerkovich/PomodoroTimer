from django import forms
from .models import ToDoList
from ToDo.widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class TodoForm (forms.ModelForm) :
    class Meta:
        model  = ToDoList
        fields = ["title", "dead_line", "state", "description"]
        widgets = {"dead_line":DatePickerInput () }
