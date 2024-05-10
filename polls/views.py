from django.shortcuts import render
from .models import Post

def index(request):
    posts_list = Post.objects.all()[:5]
    return render(request, "polls/index.html",{"Post": posts_list})
