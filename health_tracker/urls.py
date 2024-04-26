# urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls', namespace='users')),
    path('activities/', include('activities.urls', namespace='activities')),
    path('reminders/', include('reminders.urls', namespace='reminders')),
    path('community/', include('community.urls', namespace='community')),
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
]