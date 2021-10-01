from django.db import models
from embed_video.fields import EmbedVideoField


class video(models.Model):
    name= models.CharField(max_length=500)
    videolink=EmbedVideoField(blank=True)
    text=models.TextField(blank=True)

    def __str__(self):
        return self.name
