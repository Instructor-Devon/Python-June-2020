from django.shortcuts import render, redirect
from .models import User, Post
# Create your views here.
def index(request):
    # logging in a user!
    
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

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
    return redirect('/')

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