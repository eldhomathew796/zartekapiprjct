from django.shortcuts import render
from .serializers import PostSerializers,UserSerialixer
from .models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.views import APIView


# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated,)
    queryset=Post.objects.all().order_by('-date_created')
    serializer_class=PostSerializers
    filter_backends=(filters.BaseFilterBackend,filters.OrderingFilter,filters.SearchFilter)#filters.DjangoFilterBackend
    filter_fields=('liked',)
    
    ordering=('-date_created',)
    search_fields=('post_title',)
class UnLikedPostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-date_created').filter(liked=False)
    serializer_class=PostSerializers
    
class CreateuserView(CreateAPIView): 
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerialixer   
    
class LikedTaskViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-date_created').filter(liked=True)
    serializer_class=PostSerializers  



class PostViewset(viewsets.ModelViewSet):
    # permission_classes =(IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializers 
    




class PostViewDelete(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializers 
    
    
    @action(detail=True, methods=['DELETE'])
    def delete_object(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)









@api_view(['GET'])
def Post_Details(request, pk):
    qs = Post.objects.filter(id=pk)
    serializers = PostSerializers(qs, many=True)
    return Response(serializers.data)







@api_view(['DELETE'])
def Post_Delete(request, pk):
    qs = Post.objects.filter(id=pk).first()
    qs.delete()
    return Response("Deleted successfully")


# Update post
@api_view(['PATCH',"PUT"])
def Post_Update(request, pk):
    qs = Post.objects.filter(id=pk).first()
    
    serializer = PostSerializers(instance=qs,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




# class PostViewsetview(APIView):
    # permission_classes =(IsAuthenticated,)
    # queryset=Post.objects.all()
    # serializer_class=PostSerializers 
    # parser_classes=(MultiPartParser,FormParser)

    