from django.db import models

# Create your models here.
class Event(models.Model):
  eventfulID = models.IntegerField()
  date = models.DateField()
  duration = models.DurationField()
  category = models.TextField()
  title = models.TextField()
  location = models.TextField()
  venue = models.TextField()
  longitude = models.FloatField()
  latitude = models.FloatField()
  poster = models.ImageField()

class Picture(models.Model):
  path = models.ImageField()
  event = models.ForeignKey(Event)
  luminosity = models.IntegerField()
  # other img properties

class Mosaic(models.Model):
  event = models.ForeignKey(Event)

class Mosaic_cell(models.Model):
  mosaic = models.ForeignKey(Mosaic)
  picture = models.ForeignKey(Picture)
  row = models.IntegerField()
  column = models.IntegerField()