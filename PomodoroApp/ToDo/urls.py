from .views import todo_page, item_delete
from django.urls import path, include, re_path


urlpatterns = [
    path('', todo_page),
    re_path (r'^delete/(?P<pk>[0-9]+)/$', item_delete, name='item_delete'),
]
