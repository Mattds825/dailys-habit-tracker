from . import views
from django.urls import path

urlpatterns = [
    path('explore/', views.BrowseHabits.as_view(), name='explore'),
    path('<str:user>/', views.user_habits, name='user_habits'),
]
