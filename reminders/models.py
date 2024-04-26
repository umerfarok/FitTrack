# models.py
from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title