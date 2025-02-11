from django.shortcuts import render
from django.views import generic
from .models import Habit, CheckIn

# Create your views here.

class BrowseHabits(generic.ListView):
    queryset = Habit.objects.all().filter(visibility=2)
    template_name = "habit_tracker/explore_habits.html"
    paginate_by = 5
    
