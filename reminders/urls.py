# urls.py
from django.urls import path
from . import views

app_name = 'reminders'
urlpatterns = [
    path('create/', views.create_reminder, name='create_reminder'),
    path('view/', views.view_reminder, name='view_reminder'),
]