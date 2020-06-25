from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('posts', views.posts),
    path('login', views.login),
    path('posts/create', views.create_post)
]