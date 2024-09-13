from django.urls import path
from . import views

# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search
from .views import PostByTagListView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
      # URL for viewing a specific post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL for creating a new comment on a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    
    # URL for updating a specific comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    
    # URL for deleting a specific comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]


urlpatterns = [
    # Search URL
    path('search/', search, name='search'),
    
    # URL for filtering posts by tag
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]