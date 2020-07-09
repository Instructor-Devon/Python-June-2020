from django.db import models
import re

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def get_all_by_email(self):
        return self.order_by('email')

    def validate(self, form_data):
        
        errors = {}
        if len(form_data['first_name']) < 1:
            errors['first_name'] = 'First Name field is required.'

        if len(form_data['last_name']) < 1:
            errors['last_name'] = 'Last Name field is required.'

        if len(form_data['email']) < 1:
            errors['email'] = 'Email field is required.'

        if len(form_data['age']) < 1:
            errors['age'] ='Age field is required.'

        if not EMAIL_MATCH.match(form_data['email']):
            errors['email'] = 'Invalid Email.'
        
        # prevent duplicate emails!
        users_with_email = self.filter(email=form_data['email'])
        if users_with_email: # if NON-EMPTY list
            errors['email'] = 'Email already in use.'

        return errors
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

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"