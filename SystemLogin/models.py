from contextlib import nullcontext
from distutils.command.upload import upload
import email
from email.mime import image
from statistics import mode
from sys import maxsize
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    address = models.CharField(max_length=50, null=True, blank=True)


class Homedetails(models.Model):
    comp_name = models.CharField(max_length=50, null=True, blank=True)
    comp_title = models.CharField(max_length=1000, null=True, blank=True)
    comp_title_two = models.CharField(max_length=1000, null=True, blank=True)
    comp_details = models.TextField(max_length=2000, null=True, blank=True)
    comp_details_two = models.TextField(max_length=2000, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    notice = models.TextField(max_length=2000, null=True, blank=True)
