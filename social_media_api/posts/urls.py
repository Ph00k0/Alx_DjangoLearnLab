from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
