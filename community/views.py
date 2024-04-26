# views.py
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def connect(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/connect.html', {'posts': posts})