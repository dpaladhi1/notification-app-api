"""
database models
"""
    
from datetime import datetime
import uuid
import os
from django.conf import settings

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

def notification_image_file_path(instance, filename):
    """ Generate notification for new file path image """
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'notification', filename)

class UserManager(BaseUserManager):
    """Managers for user"""

    def create_user(self, email, password=None, **extra_fields):
        """create,save and return a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """create and save super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)

    object = UserManager()

    USERNAME_FIELD = 'email'

class Notification(models.Model):
    title = models.CharField(max_length=1024)
    type = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    status = models.CharField(max_length=255,blank=True)
    createdate =models.DateField(auto_now=True)
    createtime =models.TimeField(auto_now=True)
    short_description = models.CharField(max_length=10000,blank=True)
    content = models.CharField(max_length=50000, blank=True)
    url = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(null=True, upload_to=notification_image_file_path)

    def __str__(self):
        return self.title
