# urls.py
from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('connect/', views.connect, name='connect'),
]