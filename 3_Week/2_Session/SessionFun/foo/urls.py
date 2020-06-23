from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/foo
    path('', views.index),
    path('create', views.create),
]