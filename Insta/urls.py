"""InstaJZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from Insta.views import (HelloWorld, PostView, PostDetailView, PostCreateView, PostUpdateView, 
PostDeleteView, addLike, UserDetailView, addComment, UserUpdateView, toggleFollow, 
ProfileSearchView, ProfileSearchResultView)

urlpatterns = [
    path('', PostView.as_view(), name='welcome'),
    path('helloworld/', HelloWorld.as_view(), name='helloworld'),
    path('posts/', PostView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('like/', addLike, name='addLike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('comment/', addComment, name='addComment'),
    path('togglefollow/', toggleFollow, name='toggleFollow'),
    path('search/result/', ProfileSearchResultView.as_view(), name='user_search_result'),
    path('search/', ProfileSearchView.as_view(), name='user_search')
]
