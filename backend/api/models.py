from django.db import models

# Create your models here.
class Melon(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    date = models.DateTimeField()
    time = models.IntegerField()

class Bugs(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    date = models.DateTimeField()
    time = models.IntegerField()
    
class Genie(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.IntegerField()
    coverImg = models.URLField()
    date = models.DateTimeField()
    time = models.IntegerField()
