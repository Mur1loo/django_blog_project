from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    tittle = models.CharField(max_length=50, null = True)
    image = models.ImageField(default="default.png", blank=True)
    subtittle = models.CharField(max_length=200)
    tags = TaggableManager()
    text = models.TextField(null = True)
    data_published = models.DateTimeField("data published", auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def initial_text(self):
        return self.text[:100]+"..."