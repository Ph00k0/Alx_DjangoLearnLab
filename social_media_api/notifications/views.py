from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    for notification in notifications:
        notification.read = True  # Mark notifications as read
        notification.save()
    
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


# Create your views here.
