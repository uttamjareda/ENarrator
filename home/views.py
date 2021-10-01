from django.shortcuts import render
from vocab.models import Word
# Create your views here.

def home(request):
    latest_word = Word.objects.order_by('-id')[0]
    print(latest_word.new_word)
    return render(request,'home/home.html',{'word':latest_word})
