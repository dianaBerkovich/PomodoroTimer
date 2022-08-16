from .views import timer_page
from django.urls import path, include

urlpatterns = [
    path('', timer_page),
]
