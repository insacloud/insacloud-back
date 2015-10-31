from django.db import models
from django.conf import settings

# import uuid
# def get_upload_to(instance, filename):
#     instance.uuid = uuid.uuid4().hex
#     return settings.UPLOAD_PATH+'%s/%s' % (instance.uuid, filename)

# import os
# from django.db import models
# def get_upload_to(instance, filename):
#   return os.path.join('photos', str(instance.id), filename)

def upload_path_handler(instance, filename):
  import os.path
  fn, ext = os.path.splitext(filename)
  return settings.UPLOAD_PATH+"{id}{ext}".format(id=instance.event.id, ext=ext)

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
  latitude = models.FloatField()
  longitude = models.FloatField()
  poster = models.ImageField(upload_to=settings.UPLOAD_PATH)

class Picture(models.Model):
  event = models.ForeignKey(Event)
  hue = models.IntegerField()
  image=models.ImageField(upload_to=upload_path_handler, null=True)
  # other img properties

class Mosaic(models.Model):
  event = models.ForeignKey(Event)

class Mosaic_cell(models.Model):
  mosaic = models.ForeignKey(Mosaic)
  picture = models.ForeignKey(Picture)
  row = models.IntegerField()
  column = models.IntegerField()
