from django.db import models
class UserManager(models.Manager):
    def email_available(self, email):
        users = self.filter(email=email)
        if len(users) > 0:
            return False
        return True
# Create your models here.
class User(models.Model):
    # here's where the fields go!
    # first_name VARCHAR(255)
    # id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField
    # posts
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    content = models.TextField()
    
    # who made the post!
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    # timestamp!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes!
    # comments