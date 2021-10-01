from django.db import models

# Create your models here.
class Word(models.Model):
    new_word = models.CharField(max_length=100)
    meaning = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.new_word