"""
serializers for notification model
"""
from rest_framework import serializers
from core.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """ serializers for notification"""
    createdate = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Notification
        fields = ['id', 'title', 'type', 'language', 'issued_by', 'status', 'createdate', 'createtime', 'short_description', 'content', 'url', 'image']
        read_only_fields = ['id', 'createdate', 'createtime', 'image']

class NotificationImageSerializer(serializers.ModelSerializer):
    """ serializers for notification image"""
    class Meta:
        model = Notification
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'} }