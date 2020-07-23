from django.shortcuts import render, redirect
from .models import Wedding
from home.models import User
from django.contrib import messages
# Create your views here.
def dashboard(request):
    context = {
        'weddings': Wedding.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'weddings/dashboard.html', context)

def new(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'weddings/new.html', context)

def create(request):
    # request.POST has the data from the form!!!
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    errors = Wedding.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)

        return redirect('/weddings/new')
    Wedding.objects.create(
        wedder_one=request.POST['one'],
        wedder_two=request.POST['two'],
        date=request.POST['date'],
        planner=user_that_logged_in
    )
    return redirect('/weddings')