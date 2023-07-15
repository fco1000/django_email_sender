from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    pass
    #make sure to install pillow
    def __str__(self):
        return f'{self.username}'
    
   