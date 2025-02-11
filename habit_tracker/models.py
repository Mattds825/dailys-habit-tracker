from django.db import models
from django.contrib.auth.models import User

VIS_STATUS = ((0, "Private"), (1, "Follower"), (2, "Public"))
CHOSEN_COLOR = ((0, "Red"), (1, "Green"), (2, "Blue"), (3, "Yellow"), (4, "Purple"), (5, "Orange"), (6, "Pink"), (7, "Gray"))

# Create your models here.

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    title = models.CharField(max_length=100)    
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    color = models.IntegerField(choices=CHOSEN_COLOR, default=0)
    visibility = models.IntegerField(choices=VIS_STATUS, default=0)

    def __str__(self):
        return self.title
    
    
class CheckIn(models.Model):    
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="check_ins")
    checked_in_on = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()