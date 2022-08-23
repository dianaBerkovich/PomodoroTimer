from .views import todo_page
from django.urls import path, include, re_path


urlpatterns = [
    path('', todo_page, name = 'todo_page'),

]
