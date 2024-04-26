# models.py
from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.DurationField()
    date = models.DateField()
    calories_burned = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"