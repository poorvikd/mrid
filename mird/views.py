from django.shortcuts import render
from .models import *
from datetime import date,datetime, timedelta
# Create your views here.
def index(request):
    if datetime.now().date() == date.fromisoformat("2020-11-10"):
        context={}
        context["bday"]=True
        return render(request, "mird/index.html",context)
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
    if datetime.now().date() == date.fromisoformat("2020-11-10"):
        video_files = Video.objects.all()
        context={}
        context["video_exists"]=True
        context["videos"]=video_files
        return render(request, "mird/video-list.html",context)
    else:
        context={}
        context["video_exists"]=False
        return render(request, "mird/video-list.html", context)
 
def games(request,game_id):
    return render(request, f"mird/game_{game_id}.html")
def games_list(request):
    context={}
    games = {1: date.fromisoformat("2020-11-03"),
             2: date.fromisoformat("2020-11-04"),
             3: date.fromisoformat("2020-11-05"),
             4: date.fromisoformat("2020-11-06"),
             5: date.fromisoformat("2020-11-07"),
             6: date.fromisoformat("2020-11-08"),
             7: date.fromisoformat("2020-11-09"),
             8: date.fromisoformat("2020-11-10")}
    for i in range(1,9):
        if datetime.now().date() == games[i]:
            context["len"]=range(1,i+1)
    
    return render(request,"mird/games.html",context)
def redeem(request):
    context={}
    if request.method=="POST":
        code= request.POST['code']
        vids = Video.objects.filter(game_code = code)
        if vids.exists():
            context = {}
            context["video_exists"]=True
            context["videos"] = vids
            return render(request, "mird/video-list.html",context)
        elif code == "QX78HRT74":   
            context = {}
            context["video_exists"]=True
            context["videos"] = Video.objects.all()
            return render(request, "mird/video-list.html", context)

        else:
            context["error"]=True
            context["error_message"]="Please enter a valid code"
    return render(request,"mird/redeem.html",context)
