from django.db import models
from datetime import datetime
import bcrypt

class UserManager(models.Manager):
    def get_all_by_username(self):
        return self.order_by('username')

    def register(self, form_data):
        my_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            password=my_hash,
            username=form_data['username'],
        )

    def authenticate(self, username, password):
        # return True/False
        users_with_username = self.filter(username=username)
        if not users_with_username:
            return False
        user = users_with_username[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def validate(self, form_data):
        
        errors = {}
        if len(form_data['first_name']) < 1:
            errors['first_name'] = 'First Name field is required.'

        if len(form_data['last_name']) < 1:
            errors['last_name'] = 'Last Name field is required.'

        if len(form_data['username']) < 5:
            errors['username'] = 'Username must be at least 5 characters.'


        if form_data['password'] != form_data['confirm']:
            errors['password'] = "Passwords do not match"
        
        # prevent duplicate usernames!
        users_with_username = self.filter(username=form_data['username'])
        if users_with_username: # if NON-EMPTY list
            errors['username'] = 'username already in use.'

        return errors
# Create your models here.
class User(models.Model):
    # here's where the fields go!
    # first_name VARCHAR(255)
    # id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # posts => [{POST}, {POST}]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

