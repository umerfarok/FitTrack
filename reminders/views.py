# views.py
from django.shortcuts import render, redirect
from .forms import ReminderForm
from .models import Reminder
from django.contrib.auth.decorators import login_required

@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminders:view_reminder')
    else:
        form = ReminderForm()
    return render(request, 'reminders/create_reminder.html', {'form': form})

@login_required
def view_reminder(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminders/view_reminder.html', {'reminders': reminders})