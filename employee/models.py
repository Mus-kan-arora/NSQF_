from django.shortcuts import render,redirect
from decimal import Decimal
from NSQF import settings
from .models import *
from django.contrib.auth import login,logout,authenticate
from datetime import date
# Create your models here.
from django.db import models
# Create your models here.
import datetime

# Create your models here.
class TP(models.Model):
    Cat=models.CharField(max_length=100,default="X")
    Batch_Code = models.CharField(max_length=100)
    Roll_No = models.CharField(max_length=100)
    Course_Name = models.CharField(max_length=100,default='certified computer application accounting and publishing',null=True)
    Registration_number = models.IntegerField(null=True)
    Name_of_the_Candidate = models.CharField(max_length=100)
    Mother_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    DOB = models.DateField(null=True)
    Name_of_the_training_Partner = models.CharField(max_length=200)
    Code_of_the_training_Partner = models.CharField(max_length=200)
    Practical1 = models.CharField(max_length=100)
    Practical2 = models.CharField(max_length=100)
    IS1 = models.CharField(max_length= 100, null= True )
    IS2 = models.CharField(max_length= 100, null = True)
    Internal_Assessment = models.IntegerField(null=True)
    Project = models.CharField(max_length=100)
    Major_Project = models.CharField(max_length=100, default='NA')
    Major_Project2 = models.CharField(max_length=100, default='NA')
    Typing_Speed=models.CharField(max_length=100, default='NA')
    Theory1=models.CharField(max_length=100, default='NA')
    Theory2=models.CharField(max_length=100, default='NA')
    # Total=models.CharField(max_length=100, default='NA')
    Center_code = models.CharField(max_length=100,  default='NA')
    Total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    Date_of_Exam = models.DateField(null=True)
    def __str__(self):
        return self.Course_Name
