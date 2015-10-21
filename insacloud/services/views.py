from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from services.models import Event, Picture, Mosaic, Mosaic_cell
from services.serializers import UserSerializer, GroupSerializer, EventSerializer, PictureSerializer, MosaicSerializer, Mosaic_cellSerializer
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer

  def perform_create(self, serializer):
    import os
    event = serializer.save()
    buff = event.poster.name
    fn, ext = os.path.splitext(event.poster.name)
    event.poster.name = settings.UPLOAD_PATH+"poster_{id}{ext}".format(id=event.id, ext=ext)
    os.rename(buff, event.poster.name)
    event.save()

  def get_queryset(self):
    """
    Optionally restricts the returned purchases to a given user,
    by filtering against a `username` query parameter in the URL.
    """
    queryset = Event.objects.all()
    longitude = self.request.query_params.get('longitude', None)
    latitude = self.request.query_params.get('latitude', None)
    if longitude is not None and latitude is not None:
      print("o")
      queryset = queryset.filter(Event__longitude=longitude)
    return queryset

class PictureViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

  def perform_create(self, serializer):
    import os
    picture = serializer.save()
    buff = picture.image.name
    fn, ext = os.path.splitext(picture.image.name)
    picture.image.name = settings.UPLOAD_PATH+"{eventId}_{id}{ext}".format(id=picture.id, eventId=picture.event.id, ext=ext)
    os.rename(buff, picture.image.name)
    picture.save()

class MosaicViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Mosaic.objects.all()
  serializer_class = MosaicSerializer

class Mosaic_cellViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Mosaic_cell.objects.all()
  serializer_class = Mosaic_cellSerializer