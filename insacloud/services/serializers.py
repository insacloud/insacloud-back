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
    fields = ('url', 'eventfulID', 'date', 'duration', 'category', 'title', 'location', 'venue', 'longitude', 'latitude', 'poster')

class PictureSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Picture
    fields = ('url', 'event', 'hue', 'image')

  # def perform_update(self, serializer):
  #   old_obj = self.get_object()
  #   new_data_dict = serializer.validated_data
  #   serializer.save()
  #   serializer.image = serializer.id
  #   serializer.save()
  #   return "serializer"

# def perform_create(self, serializer):
#     # Include the owner attribute directly, rather than from request data.
#     instance = serializer
#     # Perform a custom post-save action.
#     instance.image=instance.id
#     instance.save()
#     return instance

  # def post_save(self, validated_data):
  #   # picture = Picture.objects.create(**validated_data)
  #   # picture.save()
  #   # picture.image = picture.id
  #   # return picture
  #   self.object.image=self.object.id
  #   self.object.save()
  #   return self.object

class MosaicSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Mosaic
    fields = ('url', 'event')

class Mosaic_cellSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Mosaic_cell
    fields = ('url', 'mosaic', 'picture', 'row', 'column')