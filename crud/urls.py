from django.conf.urls import url
from django.urls import path, include, re_path
from .views import (
    PostsListApiView,
    PostsCreateApiView,
    PostsDeleteApiView,
    PostsUpdateApiView,
    PostsDetailApiView,
)

urlpatterns = [
    path('', PostsListApiView.as_view()),
    path('create/', PostsCreateApiView.as_view(), name='create'),
    path('detail/<slug:post_slug>/', PostsDetailApiView.as_view(), name='detail'),
    path('delete/<int:post_id>/', PostsDeleteApiView.as_view(), name='delete'),
    path('update/<int:post_id>/', PostsUpdateApiView.as_view(), name='update'),
]