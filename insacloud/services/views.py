from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from services.models import Event, Picture, Mosaic
from services.serializers import UserSerializer, GroupSerializer, EventSerializer, PictureSerializer, MosaicSerializer
from services.geolocalisation import get_bounding_box
from services.mosaic.ImageFormatter import ImageFormatter
from django.conf import settings
from rest_framework.decorators import detail_route, list_route

from django.http import HttpResponse
import os
from rest_framework import serializers

def generateMosaic(enventId):
  from services.mosaic.GenerateMosaic import GenerateMosaic
  evt = Event.objects.get(pk=enventId)
  pictures = Picture.objects.filter(event=enventId)
  gn = GenerateMosaic(evt.poster, pictures)
  Mosaic.objects.filter(event=enventId).delete()
  mosaics = gn.generate(enventId, settings.MEDIA_ROOT)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

  def perform_create(self, serializer):
    if serializer.is_valid():
      user = serializer.save()
      user.set_password(user.password)
      user.is_staff = True # for demo
      user.save()

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

  @detail_route()
  def generate_mosaic(self, request, pk):
    generateMosaic(pk)

    return HttpResponse("OK")

  def perform_create(self, serializer):
    if serializer.is_valid():
      event = serializer.save()
      buff = event.poster.path
      fn, ext = os.path.splitext(buff)
      event.poster.name = "poster_{id}{ext}".format(id=event.id, ext=ext)
      os.rename(buff, settings.MEDIA_ROOT+event.poster.name)

      imf = ImageFormatter(event.poster.path)
      imf.process_image(settings.IMAGE_SIDE)
      imf.save_image(event.poster.path)

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
    if serializer.is_valid():
      picture = serializer.save()
      buff = picture.image.path
      fn, ext = os.path.splitext(picture.image.path)
      picture.image.name = "picture_{eventId}_{id}{ext}".format(id=picture.id, eventId=picture.event.id, ext=ext)
      os.rename(buff, settings.MEDIA_ROOT+picture.image.name)

      imf = ImageFormatter(picture.image.path)
      picture.hue = imf.process_image(settings.IMAGE_SIDE)
      imf.save_image(picture.image.path)

      picture.save()

      if Picture.objects.filter(event=picture.event.id).count() % int(settings.GENERATE_MOSAIC_STEP) == 0:
        generateMosaic(picture.event.id)

class MosaicViewSet(viewsets.ModelViewSet):
  queryset = Mosaic.objects.all()
  serializer_class = MosaicSerializer

  @list_route()
  def get_image(self, request, pk=None):
    import os
    from django.http import JsonResponse
    import json
    event = int(self.request.query_params.get('event', -1))
    level = int(self.request.query_params.get('level', -1))
    row = int(self.request.query_params.get('row', -1))
    column = int(self.request.query_params.get('column', -1))
    if event == -1 or not Event.objects.filter(pk=event):
      return JsonResponse({'event':'not set or not exist.'})
    elif level == -1:
      return JsonResponse({'level':'not set.'})
    else:
      args = {'event':event, 'level':level}
      if row != -1:
        args["row"] = row
      if column != -1:
        args["column"] = column
      try:
        mosaics = Mosaic.objects.filter(**args)
        data = {}
        data.setdefault('results', [])
        for mosaic in mosaics:
          data['results'].append(MosaicSerializer(mosaic).data)
        return JsonResponse(data)
      except Mosaic.DoesNotExist:
        raise APIException("Error.")
