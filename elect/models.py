from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class User(AbstractUser):
    @property
    def is_voters(self):
        if hasattr(self, 'voters'):
            return True
        return False


class Voters(models.Model):
    aadhar = models.CharField(primary_key='True', max_length=100,unique=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    location = models.CharField(max_length=30, null=True)
    votingstatus = models.BooleanField
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Parties(models.Model):
    pname =models.CharField(max_length=30, unique=True, null=True)
    nominatior = models.CharField(max_length=50, null=True)
    logo = models.ImageField
    location = models.CharField(max_length=30, null=True)