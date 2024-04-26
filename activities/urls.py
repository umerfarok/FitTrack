# urls.py
from django.urls import path
from . import views

app_name = 'activities'
urlpatterns = [
    path('log/', views.log_activity, name='log_activity'),
    path('view/', views.view_activity, name='view_activity'),
    path('visualize/', views.visualize_data, name='visualize_data'),
]