# forms.py
from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'reminder_date', 'reminder_time']