#!/usr/bin/env python
import sys
import urllib.request
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "insacloud.settings"
sys.path.append("..")
from services.models import Event
from django.core.files import File

def TryAndAddNewEvent(id_source_new,
					  source, 
					  date_start, 
					  date_end, 
					  category, 
					  title, 
					  location,
					  venue,
					  longitude,
					  latitude,
					  poster_url):
	try:
		existent = Event.objects.get(id_source=id_source_new)
	except Event.DoesNotExist:
		existent = None

	if 	existent == None:	  
		
		
		from django.core.files import File
		
		
		path = "./tmp/"
		
		if not os.path.exists(path):
			os.makedirs(path)
			
		filename, file_extension = os.path.splitext(poster_url)
			
		file = '%s/%s%s' % (path, id_source_new, file_extension)
		
		'''response = urllib.request.urlopen(poster_url)

		#open the file for writing
		fh = open(file, "w")

		# read from request while writing to file
		fh.write(str(response.read())
		fh.close()
		'''
		urllib.request.urlretrieve(poster_url, file)
		
		event = Event()
		
		event.id_source = id_source_new
		event.source = source
		event.date_start = date_start
		event.date_end = date_end
		event.category = category
		event.title = title
		event.location = location
		event.venue = venue
		event.longitude = longitude
		event.latitude = latitude
		
		with open(file, 'r') as f:
			image_file = File(f) 
			event.poster.save('%s%s' % (id_source_new, file_extension), image_file, True)
		

		os.remove(file)
		
		print ("\n\n\nOK--- Event Added to database\n\n\n")
		

	else:
		print ("\n\n\nWARNING--- Event already exists (IGNORED)\n\n\n")
