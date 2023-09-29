from django.urls import path, include
from .views import PostsListView, PostDetail

urlpatterns = [
    path('', PostsListView.as_view(), name='index'),
    path('post/{int:pk}', PostDetail.as_view(), name="Post_detail")
]