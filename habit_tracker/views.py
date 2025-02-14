from django.shortcuts import render, get_list_or_404, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Habit, CheckIn
from .forms import HabitForm, CheckInForm

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
    
    if request.method == "POST":
        habit_form = HabitForm(data=request.POST)        
        if habit_form.is_valid():
            new_habit = habit_form.save(commit=False)
            new_habit.user = request.user
            new_habit.save()
            messages.add_message(request, messages.SUCCESS, "Habit added successfully")
    
    habit_form = HabitForm()
    checkin_form = CheckInForm()
   
    # get check-ins for each habit with dates
    for h in habits:        
        if h.check_ins.all():
            print(h.check_ins.all().count())
            for c in h.check_ins.all():
                print(c.checked_in_on.date())
            
    
    # user = get_list_or_404(queryset, user=user)
    return render(request, 'habit_tracker/user_habits.html', 
                  {'habits': habits,
                   'h_user': user,
                    'habit_form': habit_form,
                    'checkin_form': checkin_form
                   }
            )    
    
def edit_habit(request, user, habit_id):
    """
    edits a habit and redirects to user_habits
    """
    queryset = Habit.objects.all()
    habits = [h for h in queryset if h.user.username == user]
    habit = get_object_or_404(Habit, id=habit_id)
    
    print("edit habit")
    
    if habit.user == request.user:
        if request.method == "POST":
            habit_form = HabitForm(data=request.POST, instance=habit)
            if habit_form.is_valid():
                habit_form.save()
                messages.add_message(request, messages.SUCCESS, "Habit updated successfully")
                return HttpResponseRedirect(reverse("user_habits", args=[user]))
        else:
            habit_form = HabitForm(instance=habit)
            
        return render(request, 'habit_tracker/edit_habit.html', 
                      {'habit_form': habit_form,
                       'habit': habit
                       }
                )
    else:
        return HttpResponseRedirect(reverse("user_habits", args=[user]))

def delete_habit(request, user, habit_id):
    """
    delete a habit
    """
    queryset = Habit.objects.all()
    habits = [h for h in queryset if h.user.username == user]
    habit = get_object_or_404(Habit, id=habit_id)
    
    if habit.user == request.user:
        habit.delete()
        messages.add_message(request, messages.SUCCESS, "Habit deleted successfully")
        
    return HttpResponseRedirect(reverse("user_habits", args=[user]))

def check_in(request, user, habit_id):
    """
    check in to a habit
    """
    queryset = Habit.objects.all()
    habits = [h for h in queryset if h.user.username == user]
    habit = get_object_or_404(Habit, id=habit_id)
    
    if habit.user == request.user:
        if request.method == "POST":
            check_in_form = CheckInForm(data=request.POST)
            if check_in_form.is_valid():
                new_check_in = check_in_form.save(commit=False)
                new_check_in.habit = habit
                new_check_in.save()
                messages.add_message(request, messages.SUCCESS, "Checked in successfully")
                return HttpResponseRedirect(reverse("user_habits", args=[user]))
        
    return HttpResponseRedirect(reverse("user_habits", args=[user]))
    