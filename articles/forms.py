from django import forms
from froala_editor.widgets import FroalaEditor
from . import models

class CreateArticle(forms.ModelForm):
    
    body=forms.CharField(widget=FroalaEditor)
    class Meta:
        model=models.Article
        fields={"title", "body", "slug", "thumb"}
        