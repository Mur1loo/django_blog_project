from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from . import forms

from .models import Post

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        """Return a list of all posts."""
        return Post.objects.order_by("-data_published")

class DetailView(generic.DetailView):
    model = Post
    template_name = "polls/detail.html"

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save in the db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:index')
    else:
        form = forms.CreatePost()
        return render(request, 'polls/create.html', context={'form': form})