from .views import todo_page, delete_item, update_item, updaterecord_item,delete_all
from django.urls import path, include, re_path


urlpatterns = [
    path('', todo_page, name = 'todo_page'),
    path('delete/<int:id>', delete_item, name='delete'),
    path('update/<int:id>', update_item, name='update'),
    path('update/updaterecord/<int:id>', updaterecord_item, name='updaterecord'),
    path('delete_all/', delete_all, name='delete_all'),
]
