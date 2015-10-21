from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from services.models import Event, Picture, Mosaic, Mosaic_cell
from services.serializers import UserSerializer, GroupSerializer, EventSerializer, PictureSerializer, MosaicSerializer, Mosaic_cellSerializer


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

class PictureViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer

  def perform_create(self, serializer):
    # Include the owner attribute directly, rather than from request data.
    picture = serializer.save()
    picture.hue = picture.id
    picture.save()
    # Perform a custom post-save action.
    #instance.image=instance.hue
    #return instance

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