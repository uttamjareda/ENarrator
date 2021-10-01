from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageShow

# Create your views here.
def gallery_homepage(request):
    images_list = ImageShow.objects.all()
    count = ImageShow.objects.count()
    return render(request,'gallery/gallery.html',{'images_list':images_list , 'count':count})