""" URL for notification APP """
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from notification import views

router = DefaultRouter()
router.register('notifications', views.NotificationViewSet)

app_name = 'notification'

urlpatterns = [
    path('', include(router.urls)),
]