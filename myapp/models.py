from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models. DateTimeField('data published')

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=r'C:\Users\Clinton Cunha\Desktop\Desktop\Weekly Activities\Week17\Django\mysite\myapp')

    def __str__(self):
        return self.title