 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from tinymce.models import HTMLField
from froala_editor.fields import FroalaField

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body=HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default="default.png", blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
            a= self.body[0:10]+ "..."
            return a
            
        
         
