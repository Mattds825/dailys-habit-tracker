from django.contrib import admin
from .models import Habit, CheckIn, Reaction, FollowerLookup
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Habit)
class HabitAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'created_on', 'visibility')
    search_fields = ('title', 'description')
    list_filter = ('user', 'visibility')

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('habit', 'checked_in_on')
    search_fields = ('habit', 'notes')
    list_filter = ('habit', 'checked_in_on')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('reaction_type', 'to_habit', 'from_user', 'is_seen', 'date_created')
    search_fields = ('reaction_type', 'to_habit', 'from_user')
    list_filter = ('reaction_type', 'to_habit', 'from_user', 'is_seen', 'date_created')

@admin.register(FollowerLookup)
class FollowerLookupAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')
    search_fields = ('user', 'followed_user')
    list_filter = ('user', 'followed_user')