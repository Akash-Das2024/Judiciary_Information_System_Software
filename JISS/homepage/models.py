

from django.db import models
from django.contrib.auth.models import User



class MyUsers(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    is_registrar = models.BooleanField(default=False)
    is_judge = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)
    

class user_details(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)




    