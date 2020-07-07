from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # favorite_songs

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, related_name='favorite_songs')

class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='reviews_written', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name='reviews_received', on_delete=models.CASCADE)