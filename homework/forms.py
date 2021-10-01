
from django import forms

'''
send_mail(subject, 
        message,
        from_email, 
        recipient_list,
        fail_silently=False,
        auth_user=None, 
        auth_password=None, 
        connection=None, 
        html_message=None
        )
'''
class Homeworkform(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    authuser = forms.CharField(max_length=50,required=False)
    authpassword = forms.CharField(max_length=50,required=False)

    