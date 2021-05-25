from django.db import models

# Create your models here.



class Destination(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="")
    iso2 = models.CharField(max_length=2,default="")
    iso3 = models.CharField(max_length=3,default="")
    desc = models.TextField()
    price = models.IntegerField()
    img1 = models.TextField(default="")
    img2 = models.TextField(default="")
    img3 = models.TextField(default="")
    img4 = models.TextField(default="")

