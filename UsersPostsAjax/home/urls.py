from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('fetch', views.fetch_users),
    path('email_check', views.email_check),
    path('posts', views.posts),
    path('login', views.login),
    path('<int:user_id>/delete', views.delete),
    path('posts/create', views.create_post)
]