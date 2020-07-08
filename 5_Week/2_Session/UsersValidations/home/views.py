from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        age=request.POST['age'],
        email=request.POST['email'],
    )
    return redirect('/')

def show(request, user_id):
    print(user_id, "is user id!")
    # user profile page
    # prevent user not found!
    # [user] or []
    users_with_user_id = User.objects.filter(id=user_id)
    if len(users_with_user_id) < 1:
        # no user found with this id!
        return redirect('/')
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'show.html', context)