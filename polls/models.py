from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    tittle = models.CharField(max_length=50, null = True)
    #image = models.ImageField()
    subtittle = models.CharField(max_length=200)
    tags = TaggableManager()
    text = models.TextField(null = True)
    data_published = models.DateTimeField("data published")

    def initial_text(self):
        return self.text[:100]+"..."