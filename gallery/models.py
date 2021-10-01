from django.db import models


# Create your models here.
class ImageShow(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='1.jpg',blank=True )