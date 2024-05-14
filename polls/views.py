from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        """Return a list of all the posts."""
        return Post.objects.order_by("-data_published")

class DetailView(generic.DetailView):
    model = Post
    template_name = "polls/detail.html"