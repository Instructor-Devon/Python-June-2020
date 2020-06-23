# define my routes
from django.urls import path
from . import views
urlpatterns = [
    # localhost:8080
    path('', views.index),
    # localhost:8080/create
    path('create', views.create),
    # localhost:8080/game
    path('game', views.game),
    # localhost:8080/click
    path('click', views.click),
    # localhost:8080/reset
    path('reset', views.reset)
]