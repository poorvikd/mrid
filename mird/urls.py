from django.urls import include,path
from .views import *
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
urlpatterns = [path('',index,name='index'),
               path('video/<int:video_id>',video,name='video'), 
               path('video',video_menu,name='menu'),
               path('games',games_list,name="games_list"),
               path('games/<int:game_id>',games,name="games"),
               path('redeem',redeem,name='redeem'),] 
