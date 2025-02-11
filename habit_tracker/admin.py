from django.contrib import admin
from .models import Habit, CheckIn
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