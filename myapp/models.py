from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
# Create your models here.
#class Book(models.Model):
#    title = models.CharField(max_length=200)
#    pub_date = models. DateTimeField('data published')

class Image(models.Model):
    #title = models.CharField(max_length=200)
    #image = models.ImageField(upload_to=r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp')
    image = models.ImageField(upload_to=r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp')
    file = models.FileField(upload_to=r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp')
    def __str__(self):
        return "done"

# Create your models here.
#class File(models.Model):
#   file = models.FileField(upload_to=r'firsttestappdjango\app')
#   image = models.ImageField(upload_to=r'firsttestappdjango\app')

#class WorkSheet(models.Model):
#    worksheet_name = models.CharField(max_length= 150, default = True)
#    creator = models.ForeignKey(User, default = True)
#    worksheet_file = models.FileField(upload_to = 'worksheets', default = True)
#    number_of_stars = models.PositiveIntegerField(default = True)
#    category = models.CharField(max_length = 100, default = 0)