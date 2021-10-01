from django.shortcuts import render
from .models import video
# Create your views here.
def videopage(request):
    count=video.objects.count()
    vide=video.objects.get(id=count)
    return render(request,'video/videopage.html',{'video':vide} )