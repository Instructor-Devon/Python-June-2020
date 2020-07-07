from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('like', views.like),
    path('unlike', views.unlike),
    path('songs/<int:song_id>', views.song)
]