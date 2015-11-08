#!/usr/bin/env python

import requests
import getpass

################################################################################
####################################################################### Config #
################################################################################

urlInsaCloud = 'http://localhost/api/events/'
apiInsacloud_user = input('Insacloud API user: ')
apiInsacloud_pwd = getpass.getpass('Insacloud API password: ')
urlEventful = "http://api.eventful.com/json/events/search"

config_ImportEventDataService = {
  'locations':['Lyon', 'Villeurbanne', 'Oullins', 'Decines', 'Vaulx-en-Velin',
               'Bron', 'Grenoble', 'Vienne'],
  'categories':['music', 'circus', 'movie', 'festival', 'party'],
  'image_sizes':'original'
}

################################################################################
####################################################################### Script #
################################################################################

for location in config_ImportEventDataService['locations']:
  for category in config_ImportEventDataService['categories']:
    print ("\n---------- Getting %s events from %s -------------\n" % (category, location))
    query = urlEventful + "?app_key=test_key&location=" + str(location) + "&category=" + str(category)
    response = requests.get(query)
    if (response.status_code == 200):
      events = response.json()
      if events != None and events['events'] != None:
        for event in events['events']['event']:
          if event['image'] != None and event['title'] != None and event['image']['url'] != None:
            print(event['title'])
            data = {"id_source":  event['id'],
                    "source":     "eventful",
                    "date_start": event['start_time'],
                    "date_end":   event['stop_time'],
                    'category':   category,
                    "title":      event['title'],
                    "location":   event['city_name'],
                    "venue":      event['venue_name'],
                    "latitude":   event['latitude'],
                    "longitude":  event['longitude']
            }
            posterUrl = event['image']['url'].replace('small', 'original')
            poster = requests.get(posterUrl).content
            files = {'poster': (posterUrl,
                                poster,
                                'image/jpg',
                                {'Expires': '0'})
            }

            myResponse = requests.post(urlInsaCloud, data=data, files=files, auth=(apiInsacloud_user, apiInsacloud_pwd), verify=True)
            # print(myResponse.text)