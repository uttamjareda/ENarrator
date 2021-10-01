from django import forms

'''
class Word(models.Model):
    new_word = models.CharField(max_length=100)
    meaning = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.new_word

class Homeworkform(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    authuser = forms.CharField(max_length=50,required=False)
    authpassword = forms.CharField(max_length=50,required=False)


'''

class Addwordform(forms.Form):
    word = forms.CharField(max_length=100)
    meaning = forms.CharField(widget=forms.Textarea)
    example = forms.CharField(widget=forms.Textarea)
