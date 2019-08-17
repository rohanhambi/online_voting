from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

'''
class User(AbstractUser):
    @property
    def is_voters(self):
        if hasattr(self, 'voters'):
            return True
        return False
'''


class Voters(models.Model):
    aadhar = models.CharField(primary_key='True', max_length=100,unique=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    location = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    votingstatus = models.CharField(max_length=50,choices=(('voted','voted'),('not voted','not voted')),default='not voted')

    def __str__(self):
        return self.aadhar


class Parties(models.Model):
    pname =models.CharField(max_length=30, unique=True, null=True)
    description = models.TextField(null=True)
    nominatior = models.CharField(max_length=50, null=True)
    logo = models.FileField(upload_to='post_image', blank=True)
    location = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.pname
