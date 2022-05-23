from django.db import models

# Create your models here.
class User(models.Model):
    FirstNameF = models.CharField(max_length=255)
    LastNameF = models.CharField(max_length=255)
    EmailF = models.CharField(max_length=255)
    PasswordF = models.CharField(max_length=255)
    CpasswordF = models.CharField(max_length=255)