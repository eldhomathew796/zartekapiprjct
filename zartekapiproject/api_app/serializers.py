from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
class UserSerialixer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user=get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class  Meta:
        model=get_user_model()
        fields=('username','password')




class PostSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Post
        fields = ["id","user","post_title","post_description","post_weight","liked","TotalLikes","TotalDisLikes","IsLikedOrDisLiked","date_created","image_tag","image"]