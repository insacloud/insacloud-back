from django.db import models

# Create your models here.
class Event(models.Model):
  id_source = models.IntegerField(null=True)
  source = models.CharField(max_length=2, null=True)
  date_start = models.DateTimeField(null=True)
  date_end = models.DateTimeField(null=True)
  category = models.TextField()
  title = models.TextField()
  location = models.TextField()
  venue = models.TextField()
  longitude = models.FloatField()
  latitude = models.FloatField()
  poster = models.ImageField()

class Picture(models.Model):
  event = models.ForeignKey(Event)
  hue = models.IntegerField()
  # other img properties

class Mosaic(models.Model):
  event = models.ForeignKey(Event)

class Mosaic_cell(models.Model):
  mosaic = models.ForeignKey(Mosaic)
  picture = models.ForeignKey(Picture)
  row = models.IntegerField()
  column = models.IntegerField()
