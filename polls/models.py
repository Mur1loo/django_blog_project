from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    tittle = models.CharField(max_length=50)
    image = models.ImageField()
    subtittle = models.CharField(max_length=200)
    tags = TaggableManager()
    text = models.TextField()
    data_published = models.DateTimeField("data published")

    def __str__(self):
        return self.tittle


