#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join
import getpass
import requests

# Pictures have to be placed in folder named "pictures-to-import" in current path

################################################################################
####################################################################### Config #
################################################################################

urlInsaCloud = 'http://localhost/api/pictures/'
apiInsacloud_user = input('Insacloud API user: ')
apiInsacloud_pwd = getpass.getpass('Insacloud API password: ')
eventIdFrom = int(input('Event id from (included [): '))
eventIdTo = int(input('Event id to (not included [): '))
picturesFolder = os.getcwd()+"/pictures-to-import/"

print(picturesFolder)

################################################################################
####################################################################### Script #
################################################################################

files = [ f for f in listdir(picturesFolder) if isfile(join(picturesFolder,f)) ]

for eventId in range(eventIdFrom, eventIdTo, 1):
  data = {"event": eventId}
  for f in files:
    print(f)
    image = {'image': (f, open(picturesFolder+f, 'rb'), 'image/jpg', {'Expires': '0'})}
    myResponse = requests.post(urlInsaCloud, data=data, files=image, auth=(apiInsacloud_user, apiInsacloud_pwd), verify=True)
    print(myResponse.text)
