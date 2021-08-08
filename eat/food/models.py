from django.db import models

# Create your models here.

class TopFoods(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='foodpic')
    price = models.FloatField()
    desc = models.TextField()

class CustomerSays(models.Model):
    cname = models.CharField(max_length=100)
    cimg = models.ImageField(upload_to='foodpic')
    cdesc = models.TextField()
