from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from services.models import Event, Picture, Mosaic, Mosaic_cell
from services.serializers import UserSerializer, GroupSerializer, EventSerializer, PictureSerializer, MosaicSerializer, Mosaic_cellSerializer
from services.geolocalisation import get_bounding_box
from services.mosaic.ImageFormatter import ImageFormatter
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

  def perform_create(self, serializer):
    import os
    event = serializer.save()
    buff = event.poster.name
    fn, ext = os.path.splitext(event.poster.name)
    event.poster.name = settings.UPLOAD_PATH+"poster_{id}{ext}".format(id=event.id, ext=ext)
    os.rename(buff, event.poster.name)

    imf = ImageFormatter(event.poster.name)
    imf.save_image(event.poster.name)

    event.save()

  def get_queryset(self):
    latitude = float(self.request.query_params.get('latitude', -1))
    longitude = float(self.request.query_params.get('longitude', -1))
    radius = float(self.request.query_params.get('radius', -1))
    if (latitude != -1 and longitude != -1 and radius != -1):
      boundbox = get_bounding_box(latitude,longitude,radius)
      return Event.objects.filter(latitude__gte=boundbox.lat_min, latitude__lte=boundbox.lat_max, longitude__gte=boundbox.lon_min, longitude__lte=boundbox.lon_max)
    return Event.objects.all()

class PictureViewSet(viewsets.ModelViewSet):
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

  def perform_create(self, serializer):
    import os
    picture = serializer.save()
    buff = picture.image.name
    fn, ext = os.path.splitext(picture.image.name)
    picture.image.name = settings.UPLOAD_PATH+"{eventId}_{id}{ext}".format(id=picture.id, eventId=picture.event.id, ext=ext)
    os.rename(buff, picture.image.name)
    resizeImage(picture.image.name)

    imf = ImageFormatter(picture.image.name)
    picture.hue = imf.process_image(settings.IMAGE_SIDE)
    imf.save_image(picture.image.name)

    picture.save()

class MosaicViewSet(viewsets.ModelViewSet):
  queryset = Mosaic.objects.all()
  serializer_class = MosaicSerializer

class Mosaic_cellViewSet(viewsets.ModelViewSet):
  queryset = Mosaic_cell.objects.all()
  serializer_class = Mosaic_cellSerializer