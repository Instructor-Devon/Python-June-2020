from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('ajax/users', views.users),
    path('posts', views.posts),
    path('login', views.login),
    path('posts/create', views.create_post)
]