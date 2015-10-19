#!/usr/bin/env python
import sys
import urllib2
import os
sys.path.append("..")
sys.path.append("config")
sys.path.append("services")

from models import Event

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
					  poster):
		
	existent = Event.objects.filter(id_source=id_source_new)
	if 	existent == None:	  
		event = Event(id_source_new,
						  source, 
						  date_start, 
						  date_end, 
						  category, 
						  title, 
						  location,
						  venue,
						  longitude,
						  latitude,
						  poster)
		print "OK--- Event Add to database"
	else:
		print "WARNING--- Event already exists"
	