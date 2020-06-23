from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # first time user experience
    if 'username' not in request.session:
        request.session['username'] = 'New User'
        request.session['users'] = []

    context = {
        'username': request.session['username'],
        'users': request.session['users'],
        'colors': ['green', 'red', 'blue']
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        request.session['username'] = request.POST['username']
        request.session['users'].append(request.POST['username'])
    return redirect('/')

def game(request):
    if 'username' not in request.session:
        request.session['username'] = 'New User'
    
    # check to see if I have started game
    if 'count' not in request.session:
        request.session['count'] = 0

    context = {
        'username': request.session['username'],
        'times': request.session['count']
    }
    return render(request, 'game.html', context)

def click(request):
    # HANDLE CLICK
    request.session['count'] += 1
    return redirect('/game')


def reset(request):
    # HANDLE RESET

    # REMOVE EVERYTHING FROM SESSION
    # request.session.clear()

    # REMOVE ONE THING FROM SESSION
    del request.session['count']
    return redirect('/game')