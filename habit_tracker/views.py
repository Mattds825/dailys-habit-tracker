from datetime import timedelta
from django.shortcuts import render, get_list_or_404, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count, Q
from django.utils.timezone import now
from .models import Habit, CheckIn, Reaction, User, FollowerLookup
from .forms import HabitForm, CheckInForm

# Create your views here.


class BrowseHabits(generic.ListView):
    queryset = Habit.objects.all().filter(visibility=2)
    template_name = "habit_tracker/explore_habits.html"
    paginate_by = 5


def check_redirect(request):
    """
    check if user is authenticated
    redirect to explore if authenticated
    else redirect to landing page
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("explore"))
    else:
        return HttpResponseRedirect(reverse("landing"))


def explore_habits(request):
    """
    display all public habits
    that are not associated with the logged in user
    if user is not logged in return to landing page
    """
    queryset = Habit.objects.all().filter(visibility=2)

    # only show public habits that are not associated with the logged in user
    # if not logged in return to landing page
    if request.user.is_authenticated:
        queryset = queryset.exclude(user=request.user)
    else:
        return HttpResponseRedirect(reverse("landing"))    

    habits = queryset.order_by('-created_on')
    
    # get list of followed_users from FollowerLookup 
    following_users = FollowerLookup.objects.filter(user=request.user)        
    following_users = [f.followed_user for f in following_users]

    today = now().date()
    for h in habits:
        h.streak_number = 0
        streak = 0
        for c in h.check_ins.order_by('-checked_in_on'):
            if c.checked_in_on.date() == today:
                streak += 1
            else:
                break
        h.streak_number = streak
        
    # annotate each habit with a list of check_in check_in_on dates in the format yyyy-mm-dd
    for h in habits:
        h.check_in_dates = [c.checked_in_on.strftime('%Y-%m-%d') for c in h.check_ins.all()]

    return render(request, 'habit_tracker/explore_habits.html',
                    {
                    'habits': habits, 
                    'following_users': following_users
                    }
                )


def user_habits(request, user):
    """
    display posts associated with a user
    show add post button if user is logged in
    """

    queryset = Habit.objects.all()
    today = now().date()
    # annotate habits with check_ins_today count
    habits = Habit.objects.annotate(
        check_ins_today=Count('check_ins', filter=Q(
            check_ins__checked_in_on__date=today))
    ).order_by('-created_on')

    # annotate habits with streak_number to show the current streak of consecutive check-ins
    for h in habits:
        print(h.id, h.title)
        h.streak_number = 0
        streak = 0
        check_day = today
        for c in h.check_ins.order_by('-checked_in_on'):
            # skip if multiple check-ins on the same day
            if c.checked_in_on.date() == check_day + timedelta(days=1):
                pass                 
            elif c.checked_in_on.date() == check_day:
                streak += 1
                check_day = check_day - timedelta(days=1)            
            else:
                break
        h.streak_number = streak

    # remove habits that are not associated with the user
    habits = [h for h in habits if h.user.username == user]
    
    # annotate each habit with a list of check_in check_in_on dates in the format yyyy-mm-dd
    for h in habits:
        h.check_in_dates = [c.checked_in_on.strftime('%Y-%m-%d') for c in h.check_ins.all()]
    
    # annotate user with new is_followed boolean
    if user != request.user.username:
        user = User.objects.get(username=user)
        user.is_followed = False
        for a in FollowerLookup.objects.filter(user=request.user):
            if a.followed_user == user:
                user.is_followed = True

    new_reactions = Reaction.objects.filter(
        to_habit__user=request.user, is_seen=False)

    # print(new_reactions.count())

    #  check if user is logged in and if user is the same as the user in the url
    #  add habit form
    if request.user == User.objects.get(username=user):
        if request.method == "POST":
            habit_form = HabitForm(data=request.POST)
            if habit_form.is_valid():
                new_habit = habit_form.save(commit=False)
                new_habit.user = request.user
                new_habit.save()
                messages.add_message(
                    request, messages.SUCCESS, "Habit added successfully")

    habit_form = HabitForm()
    checkin_form = CheckInForm()

    # user = get_list_or_404(queryset, user=user)
    return render(request, 'habit_tracker/user_habits.html',
                  {'habits': habits,
                   'h_user': user,
                   'habit_form': habit_form,
                   'checkin_form': checkin_form,
                   'new_reactions': new_reactions
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
                messages.add_message(
                    request, messages.SUCCESS, "Habit updated successfully")
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
        messages.add_message(request, messages.SUCCESS,
                             "Habit deleted successfully")

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
                messages.add_message(
                    request, messages.SUCCESS, "Checked in successfully")
                return HttpResponseRedirect(reverse("user_habits", args=[user]))

    return HttpResponseRedirect(reverse("user_habits", args=[user]))


def user_reaction(request, habit_id, reaction_type):
    """
    add a reaction to a habit
    """
    queryset = Habit.objects.all()
    habit = get_object_or_404(Habit, id=habit_id)

    print("reaction")

    # check if reaction is from the user
    if habit.user != request.user:
        reaction = Reaction.objects.create(
            reaction_type=reaction_type,
            to_habit=habit,
            from_user=request.user
        )
        reaction.save()
        messages.add_message(request, messages.SUCCESS,
                             "Reaction added successfully")

    # return to explore page
    return HttpResponseRedirect(reverse("explore"))


def dismiss_reaction(request, user, reaction_id):
    """
    dismiss a reaction
    """

    # make sure correct user is dismissing the reaction
    if request.user.username != user:
        return HttpResponseRedirect(reverse("explore"))

    reaction = get_object_or_404(Reaction, id=reaction_id)
    reaction.is_seen = True
    reaction.save()

    return HttpResponseRedirect(reverse("user_habits", args=[user]))


def search_users(request, user):
    """
    return a list of matching usernames to the user parameter
    should exclude the logged in user
    """

    users = User.objects.filter(username__icontains=user)

    current_user = ""

    # exclude the logged in user
    if request.user.is_authenticated:
        users = users.exclude(username=request.user.username)
        current_user = request.user

    already_following = FollowerLookup.objects.filter(user=current_user)

    print(already_following)

    # annotate users boolean is_followed if the user is in the already_followed.user_followed list
    for u in users:
        u.is_followed = False
        for a in already_following:
            if a.followed_user == u:
                u.is_followed = True

    for u in users:
        print(u.is_followed)

    return render(request, 'habit_tracker/search_users.html',
                  {'users': users}
                  )


def follow_user(request, user):
    """
    follow a user
    """

    followed_user = get_object_or_404(User, username=user)

    if request.user.is_authenticated:
        new_follow = FollowerLookup.objects.create(
            user=request.user,
            followed_user=followed_user
        )
        new_follow.save()
        messages.add_message(request, messages.SUCCESS,
                             f"started following {user}")

    return HttpResponseRedirect(reverse("search_users", args=[user]))


def unfollow_user(request, user):
    """
    unfollow a user
    """

    followed_user = get_object_or_404(User, username=user)

    if request.user.is_authenticated:
        follow = FollowerLookup.objects.get(
            user=request.user,
            followed_user=followed_user
        )
        follow.delete()
        messages.add_message(request, messages.SUCCESS,
                             f"stopped following {user}")

    return HttpResponseRedirect(reverse("search_users", args=[user]))
