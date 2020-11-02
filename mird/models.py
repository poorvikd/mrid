from django.db import models
import datetime
import embed_video
# Create your models here.
class Video(models.Model):
    first_name = models.CharField(max_length=20,null=False)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    game_code = models.CharField(max_length=30,null=False,default="H120QZPKL")
    video = models.URLField()
    def __str__(self):
        if self.last_name==None:
            return f"{self.first_name}"
        else:
            return f"{self.first_name} {self.last_name}"
        
