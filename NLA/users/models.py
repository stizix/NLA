from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False )
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)   
    languages = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    
    def __str__(self):
        return self.user.username
