from django.contrib.auth.models import User, Group
from services.models import Event, Picture, Mosaic
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'id', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'id', 'name')

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('url', 'id', 'id_source', 'source', 'date_start', 'date_end', 'category', 'title', 'location', 'venue', 'latitude', 'longitude', 'poster')

class PictureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Picture
    fields = ('url', 'id', 'event', 'hue', 'image')

class MosaicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mosaic
    fields = ('url', 'id', 'event', 'level', 'row', 'column', 'image')