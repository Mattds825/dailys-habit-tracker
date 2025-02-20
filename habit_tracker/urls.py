from . import views
from django.urls import path

urlpatterns = [
    path('explore/', views.explore_habits, name='explore'),
    path('<str:user>/', views.user_habits, name='user_habits'),
    path('<str:user>/delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('<str:user>/edit_habit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('<str:user>/check_in/<int:habit_id>/', views.check_in, name='check_in'),
    path('user_reaction/<int:habit_id>/<int:reaction_type>', views.user_reaction, name='user_reaction'),
    path('<str:user>/dismiss_reaction/<int:reaction_id>', views.dismiss_reaction, name='dismiss_reaction'),
]
