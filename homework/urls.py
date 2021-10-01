from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    #path('index/',views.index,name='homeworkIndex'),
    path('',views.assignhomework,name='assignhomework'),
    path('<int:sender_id>/<int:reciever_id>/',views.sendhomework,name='sendhomework'),
    path('shuffle',views.shuffle,name='shuffle'),

]