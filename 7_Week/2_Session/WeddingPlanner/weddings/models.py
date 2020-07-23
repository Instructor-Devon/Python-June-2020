from django.db import models
from home.models import User
# Create your models here.
from datetime import datetime

class WeddingManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['one']) < 1:
            errors['one'] = "Wedder One field required"
        if len(form_data['two']) < 1:
            errors['two'] = "Wedder Two field required"
        if len(form_data['date']) < 1:
            errors['date'] = "Date field required"
        # date is in future!
        elif (datetime.strptime(form_data['date'], "%Y-%m-%d") < datetime.now()):
            errors['date'] = "Date must be in the future!"
        
        return errors

class Wedding(models.Model):
    wedder_one = models.CharField(max_length=255)
    wedder_two = models.CharField(max_length=255)
    date = models.DateField()
    # planner_id 
    planner = models.ForeignKey(User, related_name='planned_weddings', on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='weddings_attending')

    objects = WeddingManager()