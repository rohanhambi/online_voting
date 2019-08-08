from django.db import models

# Create your models here
class Voter(models.Model):
    voter_name = models.CharField(max_length=50)
    aadhar_id = models.CharField(max_length=16)
    password = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    voting_status = models.CharField(max_length=10,choices=[('Voted','Voted'),('Not Voted','Not Voted')])
        
class Party(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=1000)
    votes = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
