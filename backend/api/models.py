from django.db import models

# Create your models here.
class Melon(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    crawlingTime = models.DateTimeField()

class Bugs(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    crawlingTime = models.DateTimeField()
    
class Genie(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    crawlingTime = models.DateTimeField()
