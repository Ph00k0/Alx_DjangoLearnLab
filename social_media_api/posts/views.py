from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from .models import Post
from rest_framework.decorators import api_view, permission_classes
from accounts.models import CustomUser  # Ensure you import your CustomUser model

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Retrieves all comments
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # You can customize this if you need to filter comments, e.g., by post
        return Comment.objects.all()  # Fetches all comments

@api_view(['GET'])
def user_feed(request):
    # Get posts from the users the current user is following
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serialized_posts = PostSerializer(posts, many=True)
    return Response(serialized_posts.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed_view(request):
    # Get the current user
    current_user = request.user
    # Get the users that the current user follows
    following_users = current_user.following.all()
    
    # Retrieve posts from followed users, ordered by creation date
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    # Serialize the posts (assuming you have a PostSerializer)
    serializer = PostSerializer(posts, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
