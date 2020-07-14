from django.shortcuts import render, redirect, HttpResponse
from .models import User, Post
# Create your views here.
def index(request):
    # logging in a user!
    context = {
        'users': User.objects.all()
    }
    
    return render(request, 'index.html', context)

def fetch_users(request):
    context = {
        'users': User.objects.all()
    }
    
    return render(request, 'users.html', context)

def email_check(request):
    print(request.POST)
    message = "Email is already taken"
    if User.objects.email_available(request.POST['email']):
        message = "Email is available"
    context = {
        'message': message
    }
    return render(request, 'email_available.html', context)

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')

def login(request):
    request.session['user_id'] = request.POST['user']
    return redirect('/posts')


def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        age=request.POST['age'],
        email=request.POST['email'],
    )
    return redirect('/fetch')

def posts(request):
    context = {
        'posts': Post.objects.order_by('-created_at'),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'posts.html', context)

def create_post(request):
    user_in_session = User.objects.get(id=request.session['user_id'])
    Post.objects.create(content=request.POST['content'], author=user_in_session)
    return redirect('/posts')