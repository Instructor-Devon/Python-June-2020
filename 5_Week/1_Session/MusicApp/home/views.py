from django.shortcuts import render, redirect
from .models import User, Song
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all(),
        'songs': Song.objects.all()
    }
    return render(request, 'index.html', context)

def song(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id),
        'not_liked': User.objects.exclude(favorite_songs__id=song_id),
        'liked': User.objects.filter(favorite_songs__id=song_id),
    }
    return render(request, 'song.html', context)


def like(request):
    # query for a user
    some_user = User.objects.get(id=request.POST['user'])
    # query for a song
    some_song = Song.objects.get(id=request.POST['song'])
    # add song to user's favorite_songs
    some_user.favorite_songs.add(some_song)
    return redirect("/")

def unlike(request):
    # query for a user
    some_user = User.objects.get(id=request.POST['user'])
    # query for a song
    some_song = Song.objects.get(id=request.POST['song'])
    # add song to user's favorite_songs
    some_user.favorite_songs.remove(some_song)
    return redirect("/")