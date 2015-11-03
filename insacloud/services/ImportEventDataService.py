#!/usr/bin/env python
import sys

import dao
from dao import EventfulDAO
from dao import EventDAO
import config
from config.import_config import config_ImportEventDataService

#test_key to change with a created key with an account
api = EventfulDAO.API('test_key', cache='.cache')
# api.login('username', 'password')


def PrintEvents(events):
	if events != None and events['events'] != None:
		for event in events['events']['event']:
			print "%s at %s" % (event['title'], event['venue_name'])

def GetEventsByTypeByLocation(eventType="music", location='Lyon', image_sizes="original"):
	events = api.call('/events/search', q=eventType, l=location)
	return events
	
def AddToDatabase(events, category, location):
	i = 0
	if events != None and events['events'] != None:
		for event in events['events']['event']:
			
			image =""
			if event['image'] != None:
				
			
			
				if event['image']['url'] != None:
					
					print "\n------ADDING new event as\n"
					id_source = event['id']
					print "id_source = %s" % (id_source)
					
					source = "ef"
					print "source = %s" % (source)
					
					title = event['title']
					print "title = %s" % (title)
					
					date_start = event['start_time']
					print "date_start = %s" % (date_start)
					
					date_end = event['stop_time']
					print "date_end = %s" % (date_end)
					
					print "category = %s" % (category)
					
					location = location
					print "location = %s" % (location)
					
					venue = event['venue_name']
					print "venue = %s" % (venue)
					
					latitude = event['latitude']
					print "latitude = %s" % (latitude)
					
					longitude = event['longitude']
					print "longitude = %s" % (longitude)
				
					image = event['image']['url']
					image = image.replace('small', 'original')
					print "image = %s" % (image)
					#i= i+1
					#file_location  = FileDAO.StorePoster(id_source, image)
					
					file_url = image
					#calling DAO
					EventDAO.TryAndAddNewEvent(
						id_source,
						source, 
						date_start, 
						date_end, 
						category, 
						title, 
						location,
						venue,
						longitude,
						latitude,
						file_url
						)
	
def ImportEvents():
	for location in config_ImportEventDataService['locations']:
		for category in config_ImportEventDataService['categories']:
			print "\n---------- Getting %s events from %s -------------\n" % (category, location)
			events = GetEventsByTypeByLocation(category, location, config_ImportEventDataService['image_sizes'])
			#PrintEvents(events)
			#Add To the database
			
			AddToDatabase(events, category, location) 
		
		
ImportEvents()