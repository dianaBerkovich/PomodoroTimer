from .views import main_page, test_page
from django.urls import path, include

urlpatterns = [
    path('', main_page),
    path ('test', test_page)
]
