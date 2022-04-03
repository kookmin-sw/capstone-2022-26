from django.db import models

# Create your models here.
class Chart(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    rank = models.IntegerField()
    like = models.IntegerField()
    img_url = models.URLField(unique=True)

class Track(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    img_url = models.URLField(unique=True)
    daybefore_rank = models.IntegerField()
    yesterday_rank = models.IntegerField()
    today_rank = models.IntegerField()