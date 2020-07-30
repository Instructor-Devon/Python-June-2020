from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import bcrypt
# Create your views here.

def index(request):
    context = {
        'reg_form': RegistrationForm(),
        'log_form': AuthenticationForm()
    }
    return render(request, 'index.html', context)

def create(request):
    # something is there for first_name!
    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        # log user in!
        login(request, user)
        return redirect('/posts')
    else:
        context = {
            'reg_form': form,
            'log_form': AuthenticationForm()
        }
    return render(request, 'index.html', context)

def do_login(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        new_user = form.get_user()
        login(request, new_user)
        return redirect('/posts')
    else:
        context = {
            'reg_form': RegistrationForm(),
            'log_form': form
        }
        return render(request, 'index.html', context)

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

def success(request):
    # only logged in users should be here!
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    
    return redirect('/')