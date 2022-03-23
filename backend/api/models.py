from django.db import models

# Create your models here.
class ChartData(models.Model):
    # site = models.CharField("site", max_length=10)
    # dateTime = models.CharField("dateTime", max_length=100)
    rank_t = models.CharField("rank_t", max_length=100)
    title_t = models.CharField("title_t", max_length=100)
    artist_t =  models.CharField("artist_t", max_length=100)
    img = models.CharField("img", max_length=100)
    like = models.CharField("like", max_length=100)