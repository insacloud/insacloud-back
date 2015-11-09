from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.dispatch import receiver
import os

def validate_image_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png',]
    if not ext in valid_extensions:
        raise ValidationError('Unsupported file extension.')

# Create your models here.
class Event(models.Model):
  id_source = models.CharField(max_length=255, unique=True)
  source = models.CharField(max_length=255, null=True)
  date_start = models.DateTimeField(null=True)
  date_end = models.DateTimeField(null=True)
  category = models.TextField(null=True)
  title = models.TextField()
  location = models.TextField(null=True)
  venue = models.TextField(null=True)
  latitude = models.FloatField()
  longitude = models.FloatField()
  poster = models.ImageField(upload_to=settings.MEDIA_ROOT, validators=[validate_image_extension])

@receiver(models.signals.post_delete, sender=Event)
def event_auto_delete_files(sender, instance, **kwargs):
    if instance.poster:
        if os.path.isfile(instance.poster.path):
            os.remove(instance.poster.path)

class Picture(models.Model):
  event = models.ForeignKey(Event)
  hue = models.IntegerField(default=-1)
  image=models.ImageField(upload_to=settings.MEDIA_ROOT, null=True)

@receiver(models.signals.post_delete, sender=Picture)
def picture_auto_delete_files(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

class Mosaic(models.Model):
  event = models.ForeignKey(Event)
  level = models.IntegerField()
  row = models.IntegerField(null=True)
  column = models.IntegerField(null=True)
  image = models.ImageField(upload_to=settings.MEDIA_ROOT, validators=[validate_image_extension])