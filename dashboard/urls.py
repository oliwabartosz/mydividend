# This is urls.py for dashboard app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]