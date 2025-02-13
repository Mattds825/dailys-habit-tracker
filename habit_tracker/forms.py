from .models import Habit
from django import forms


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'description', 'color', 'visibility']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'visibility': forms.Select(attrs={'class': 'form-select'})
        }