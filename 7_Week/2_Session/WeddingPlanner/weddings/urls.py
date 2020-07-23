from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/weddings -> views.dashboard
    path('', views.dashboard),
    # localhost:8000/weddings/new -> views.new
    path('new', views.new),
    # localhost:8000/weddings/create -> views.new
    path('create', views.create)

]