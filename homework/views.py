from django.shortcuts import render,redirect
from Oratory_site.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD
from django.http import HttpResponse
from .forms import Homeworkform
import random
from .models import Person
from django.core.mail import send_mail
import time
from django.core.exceptions import PermissionDenied


dict = {}
newlist = []


def index(request):
    return HttpResponse("<h1> now we are starting the app at oratory site yeeeee-----</h1>")

def superuseronly(function):
    def inner(request):
        if not request.user.is_superuser:
            raise PermissionDenied
        else:
            return function(request)
    return inner

@superuseronly
def shuffle(request):
    dict.clear()
    newlist.clear()
    nametoemail = Person.objects.all()
    newlist.append('blank')
    for person in nametoemail:
        newlist.append(person.name)
    length = len(newlist)-1
    
    visited = [False for i in range(length)]
    print(len(visited))
    flag,current = 0,0
    for i in range(length):
        while(not flag):
            current = random.randint(0,length-1)
            if (not(visited[current])) and current!=i:
                visited[current] = True
                dict[i+1] = current+1
                flag = 1
        flag = 0
    return render(request,'homework/assign.html',{'newlist':newlist,'dict':dict,'range':range(1,15)})  

def assignhomework(request):
    return render(request,'homework/assign.html',{'newlist':newlist,'dict':dict,'range':range(1,15)})  
'''
class HomeworkForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    authuser = forms.CharField(max_length=50)
    authpassword = forms.CharField(max_length=50)
'''

def sendhomework(request,sender_id,reciever_id):
    sender = Person.objects.get(pk=sender_id)
    reciever = Person.objects.get(pk=reciever_id)
    
    form = Homeworkform(None)
    if request.method == 'POST':
        form = Homeworkform(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_mail = form.cleaned_data['sender']
            authuser = form.cleaned_data['authuser']
            authpassword = form.cleaned_data['authpassword']
            if authpassword == 'None' and authuser == 'None':
                send_mail(subject, message, from_mail, [reciever.email],False)
            else:
                send_mail(subject, message, from_mail, [reciever.email],False, authuser, authpassword,html_message=None)
            redirect('homework:assignhomework')

    return render(request , 'homework/message.html', {'sender':sender,'reciever':reciever,'form':form})

