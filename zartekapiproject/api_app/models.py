from datetime import datetime
from distutils.command.upload import upload
from time import timezone
# from typing_extensions import NotRequired
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_title=models.CharField(max_length=50)
    post_description=models.CharField(max_length=500)
    post_weight=models.CharField(max_length=500,blank=True)
    liked=models.BooleanField(default=False)
    TotalLikes=models.CharField(max_length=500,blank=True)
    TotalDisLikes=models.CharField(max_length=500,blank=True)
    IsLikedOrDisLiked=models.IntegerField(blank=True,null=True)
    image_tag=models.CharField(max_length=500,blank=True,null=True)
    image=models.ImageField(upload_to='images/',default="Image/None/Noimage.jpg")
    date_created=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.post_title
    

    




