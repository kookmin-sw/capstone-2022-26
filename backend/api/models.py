from django.db import models

# Create your models here.
class Chart(models.Model):
    sid = models.CharField(max_length=50, primary_key=True)
    rank = models.CharField(max_length=50)
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    like = models.CharField(max_length=50)
    coverImg = models.URLField()

class Track(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    img_url = models.URLField(unique=True)
    daybefore_rank = models.IntegerField()
    yesterday_rank = models.IntegerField()
    today_rank = models.IntegerField()