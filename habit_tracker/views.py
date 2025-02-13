from django.shortcuts import render, get_list_or_404
from django.views import generic
from .models import Habit, CheckIn

# Create your views here.

class BrowseHabits(generic.ListView):
    queryset = Habit.objects.all().filter(visibility=2)
    template_name = "habit_tracker/explore_habits.html"
    paginate_by = 5

def user_habits(request, user):
    """
    display posts associated with a user
    show add post button if user is logged in
    """
    
    # print(request.user)
    
    queryset = Habit.objects.all()
    habits = [h for h in queryset if h.user.username == user]
   
    # get check-ins for each habit with dates
    for h in habits:
        if h.check_ins.all():
            for c in h.check_ins.all():
                print(c.checked_in_on.date())
            
    
    # user = get_list_or_404(queryset, user=user)
    return render(request, 'habit_tracker/user_habits.html', 
                  {'habits': habits,
                   'h_user': user
                   }
            )    
