from django.db import models
import datetime

# Create your models here.
class Video(models.Model):
    first_name = models.CharField(max_length=20,null=False)
    last_name = models.CharField(max_length=20,null=False)
    date = models.DateField(auto_now_add=True)
    video = models.FileField(blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
