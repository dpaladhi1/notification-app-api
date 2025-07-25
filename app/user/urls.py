"""
url mapping for User API
"""
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.createUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]