"""
URL configuration for zartekapiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api_app.views import PostViewset,CreateuserView
from api_app import views
from django.conf import settings
from django.conf.urls.static import static
# from api_app.views import PostViewsetview

router=routers.DefaultRouter()
router.register(r'Post',views.PostViewset)
router=routers.SimpleRouter()

router.register('Post',views.PostViewset)
router.register('Liked_Post',views.LikedTaskViewset)
router.register('UnLiked_Post',views.UnLikedPostViewset)
router.register("post-delete/<int:pk>/",views.PostViewDelete)
router.register('post-details',views.PostViewset)#list view
router.register('create-post',views.PostViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('',include('api_app.urls')),
    path('register/',views.CreateuserView.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    
    
    path('post-details/<int:pk>', views.Post_Details, name='post-details'),
    path('post-delete/<int:pk>', views.Post_Delete, name='post-delete'),
    path('post-update/<int:pk>', views.Post_Update, name='post-update'),
  
    

]
if settings.DEBUG:
   
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)