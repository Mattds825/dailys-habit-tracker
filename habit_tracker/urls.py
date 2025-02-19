from . import views
from django.urls import path

urlpatterns = [
    path('explore/', views.explore_habits, name='explore'),
    path('<str:user>/', views.user_habits, name='user_habits'),
    path('<str:user>/delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('<str:user>/edit_habit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('<str:user>/check_in/<int:habit_id>/', views.check_in, name='check_in'),
]
