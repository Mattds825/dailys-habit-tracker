from . import views
from django.urls import path

urlpatterns = [
    path('explore/', views.BrowseHabits.as_view(), name='explore'),
]
