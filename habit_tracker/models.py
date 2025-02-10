from django.db import models
from django.contrib.auth.models import User

VIS_STATUS = ((0, "Private"), (1, "Follower"), (2, "Public"))

# Create your models here.

class Habit(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    title = models.CharField(max_length=100)    
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    visibility = models.IntegerField(choices=VIS_STATUS, default=0)

    def __str__(self):
        return self.name