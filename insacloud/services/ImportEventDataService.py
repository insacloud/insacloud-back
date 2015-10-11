#!/usr/bin/env python
import sys
sys.path.append("..")
sys.path.append("DAO")
import EventfulDAO


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
	
def AddToDatabase(events, location):
	if events != None and events['events'] != None:
		for event in events['events']['event']:
			print "\n------ADDING new event as\n"
			
			externalId = event['id']
			print "externalId = %s" % (externalId)
			
			type = "eventful"
			print "type = %s" % ("eventful")
			
			title = event['title']
			print "title = %s" % (title)
			
			location = location
			print "location = %s" % (location)
			
			venue = event['venue_name']
			print "venue = %s" % (venue)
			
			latitude = event['latitude']
			print "latitude = %s" % (latitude)
			
			longitude = event['longitude']
			print "longitude = %s" % (longitude)
			
			image =""
			if event['image'] != None:
				if event['image']['url'] != None:
					image = event['image']['url']
					
			image = image.replace('small', 'original')
			print "image = %s" % (image)
	
			#use DAO to add in the database
	
def ImportEvents():
	listVilles = ['Lyon']#, 'Villeurbanne', 'Oullins', 'Decines', 'Vaulx-en-Velin', 'Bron', 'Grenoble', 'Vienne']
	for location in listVilles:
		print "\n---------- Getting musical events from %s -------------\n" % (location)
		events = GetEventsByTypeByLocation('music', location)
		PrintEvents(events)
		#Add To the database
		
		AddToDatabase(events, location) 
		
		
ImportEvents()