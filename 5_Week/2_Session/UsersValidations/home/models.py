from django.db import models

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

    # objects -> queries!

    def __str__(self):
        return f"{self.first_name} {self.last_name}"