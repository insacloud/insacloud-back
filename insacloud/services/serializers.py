from django.contrib.auth.models import User, Group
from services.models import Event, Picture, Mosaic, Mosaic_cell
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Event
    fields = ('url', 'id_source', 'source', 'date_start', 'date_end', 'title', 'location', 'venue', 'longitude', 'latitude', 'poster')

class PictureSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Picture
    fields = ('url', 'event', 'hue', 'image')

class MosaicSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Mosaic
    fields = ('url', 'event')

class Mosaic_cellSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Mosaic_cell
    fields = ('url', 'mosaic', 'picture', 'row', 'column')