# views.py
from django.shortcuts import render
from .models import Activity
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from .forms import ActivityForm
from django.shortcuts import redirect

@login_required
def log_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activities:view_activity')
    else:
        form = ActivityForm()
    return render(request, 'activities/log_activity.html', {'form': form})


@login_required
def view_activity(request):
    activities = Activity.objects.filter(user=request.user)
    return render(request, 'activities/view_activity.html', {'activities': activities})
@login_required
def visualize_data(request):
    activities = Activity.objects.filter(user=request.user)
    activity_data = []
    for activity in activities:
        activity_data.append({
            'activity_type': activity.activity_type,
            'duration': activity.duration.total_seconds() / 3600,  # Convert to hours
            'date': activity.date,
            'calories_burned': activity.calories_burned,
        })

    df = pd.DataFrame(activity_data)

    # Calories burned over time
    plt.figure(figsize=(8, 6))
    plt.plot(df['date'], df['calories_burned'])
    plt.xlabel('Date')
    plt.ylabel('Calories Burned')
    plt.title('Calories Burned Over Time')
    chart1 = plt.gcf()

    # Activity durations
    plt.figure(figsize=(8, 6))
    plt.bar(df['activity_type'], df['duration'])
    plt.xlabel('Activity Type')
    plt.ylabel('Duration (hours)')
    plt.title('Activity Durations')
    chart2 = plt.gcf()

    context = {'chart1': chart1, 'chart2': chart2}
    return render(request, 'activities/visualize_data.html', context)

