# home/urls.py

from django.urls import path
from .views import myweb_view

urlpatterns = [
    path('', myweb_view, name='myweb'),
]
