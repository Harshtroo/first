from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    gender_choice = {
        ('male','male'),
        ('female','female')
    }
    is_deleted = models.BooleanField(default=False)
    gender = models.CharField(choices=gender_choice,max_length=6)
 
    def __str__(self):
        return f" {self.username} - ID {self.id} -first name : {self.first_name}"
      
    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted = True
        self.save()
    def user_active(self):
        '''user is active or not'''
        self.is_active = True
        self.save()