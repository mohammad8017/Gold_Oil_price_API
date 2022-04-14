from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from rest_framework.authtoken.models import Token
import pyodbc 

# Create your models here.

class prices(models.Model):
    start_date = models.CharField(max_length=8)
    end_date = models.CharField(max_length=8)

