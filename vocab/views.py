from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Word
from .forms import Addwordform
# Create your views here.

def storewords(request):
    l = []
    tmp = []
    length = len(Word.objects.all())
    length1 = 0
    wrds = []
    alphabets = []
    for i in range(26):
        alphabets.append(chr(i+65))
        select = Word.objects.all().filter(new_word__startswith=chr(i+65))
        length1 = len(select)
    
        if(length1!=0):
            for j in range(length1):
                tmp.append(select[j].new_word)
                tmp.append(select[j].meaning)
                tmp.append(select[j].example)
                #print(tmp)
                l.append(tmp)
                tmp = []
            
            wrds.append([chr(i+65),len(l),l])
           
        l = []
    
    return render(request,'vocab/vocabulary.html',{'words':wrds,'alphabets':alphabets,'range':range(26)})
'''
class Word(models.Model):
    new_word = models.CharField(max_length=100)
    meaning = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.new_word

            authpassword = form.cleaned_data['authpassword']
            if authpassword == 'None' and authuser == 'None':
                send_mail(subject, message, from_mail, [reciever.email],False)
            else:
                send_mail(subject, message, from_mail, [reciever.email],False, authuser, authpassword,html_message=None)
            redirect('homework:assignhomework')

    return render(request , 'homework/message.html', {'sender':sender,'reciever':reciever,'form':form})

'''
def newword(request):
    form = Addwordform(None)
    if request.method == 'POST':
        form = Addwordform(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            meaning = form.cleaned_data['meaning']
            example = form.cleaned_data['example']
            newword = Word(new_word=word,meaning=meaning,example=example)
            newword.save()
            return redirect('vocab:storewords')
    
    return render(request,'vocab/addword.html',{'form':form})

'''
class Addwordform(forms.Form):
    word = forms.CharField(max_length=100)
    meaning = forms.TextField(widget=forms.Textarea)
    example = forms.TextField(widget=forms.Textarea)
'''


def wordslist(request):
    words= Word.objects.order_by('-id')
    return render(request, 'vocab/vocablist.html',{'words':words})

