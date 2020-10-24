from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,"mird/index.html")
def video(request,video_id):
    context={}
    lastvideo = Video.objects.filter(id=video_id)[0]
    videofile = lastvideo.video
    context["vid"]=videofile
    context["fname"]=lastvideo.first_name
    context["lname"]=lastvideo.last_name
    return render(request, "mird/video_view.html",context)
def video_menu(request):
    video_files=Video.objects.all().order_by('-date')
    context={}
    context["videos"]=video_files
    return render(request, "mird/video-list.html",context)


