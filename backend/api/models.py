from django.db import models

# Create your models here.
class Melon(models.Model):
    m_rank = models.IntegerField()
    m_song = models.CharField(max_length=50)
    m_artist = models.CharField(max_length=50)
    m_like = models.IntegerField()
    m_coverImg = models.URLField()
    m_date = models.DateTimeField()
    m_time = models.IntegerField()
    m_weight = models.FloatField(default=0)


class Bugs(models.Model):
    b_rank = models.IntegerField()
    b_song = models.CharField(max_length=50)
    b_artist = models.CharField(max_length=50)
    b_like = models.IntegerField()
    b_coverImg = models.URLField()
    b_date = models.DateTimeField()
    b_time = models.IntegerField()
    b_weight = models.FloatField(default=0)
    
class Genie(models.Model):
    g_rank = models.IntegerField()
    g_song = models.CharField(max_length=50)
    g_artist = models.CharField(max_length=50)
    g_like = models.IntegerField()
    g_coverImg = models.URLField()
    g_date = models.DateTimeField()
    g_time = models.IntegerField()
    g_weight = models.FloatField(default=0)

class Total(models.Model):
    rank = models.IntegerField()
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    coverImg = models.URLField()
    date = models.DateTimeField()
    time = models.IntegerField()
    weight = models.FloatField(default=0)
