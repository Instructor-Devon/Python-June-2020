from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    
    context = {
        'user': request.user,
        'posts': Post.objects.all(),
        'form': NewPostForm()
    }
    return render(request, 'dashboard/index.html', context)
    
def create(request):
    sent_form = NewPostForm(request.POST)
    if sent_form.is_valid():
        # create a new post
        new_post = sent_form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('/posts')
    else:
        context = {
            'user': request.user,
            'posts': Post.objects.all(),
            'form': sent_form
        }
        return render(request, 'dashboard/index.html', context)
def delete(request, post_id):
    # i want to delete a post!
    # check that the post i'm about to delete belongs to the logged in user
    to_delete = Post.objects.get(id=post_id)
    if to_delete.author_id == request.user.id:
        to_delete.delete()
    return redirect('/posts')