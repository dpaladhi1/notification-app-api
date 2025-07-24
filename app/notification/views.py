"""
views for the notification API
"""
from rest_framework import (
    viewsets,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Notification
from notification import serializers

class NotificationViewSet(viewsets.ModelViewSet):
    """ view for manage receipe API """
    serializer_class = serializers.NotificationSerializer
    queryset = Notification.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve notification order by createdatetime """
        return self.queryset.order_by('createdate')
    
    def get_serializer_class(self):
        if self.action == 'upload_image':
            return serializers.NotificationImageSerializer
        
        return self.serializer_class
    
    @action(methods=['POST'], detail=True, url_path='upload_image')
    def upload_image(self, request, pk=None):
        """ upload an image to notification"""
        notification = self.get_object()
        serializer = self.get_serializer(notification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_Bad_REQUEST)
