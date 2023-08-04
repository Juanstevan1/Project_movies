from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    year= models.CharField(default =0, max_length=100)
    duration = models.IntegerField(default=0,max_length=100)
    url = models.URLField(blank=True)