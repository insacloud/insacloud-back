#!/usr/bin/env python

from PIL import Image
import requests
from requests.auth import HTTPDigestAuth
import json
import os
import getpass

################################################################################
####################################################################### Config #
################################################################################

urlInsaCloud = 'http://localhost/api/pictures/'
apiInsacloud_user = input('Insacloud API user: ')
apiInsacloud_pwd = getpass.getpass('Insacloud API password: ')
eventId = 1
imageDim = 512

################################################################################
####################################################################### Script #
################################################################################

data = {"event": eventId}
for i in range(256):
  img = Image.new("L", (imageDim, imageDim), i)
  img.save("shade-of-grey.jpeg","JPEG")
  files = {'image': ("shade-of-grey.jpeg", open("shade-of-grey.jpeg", 'rb'), 'image/jpg', {'Expires': '0'})}
  myResponse = requests.post(urlInsaCloud, data=data, files=files, auth=(apiInsacloud_user, apiInsacloud_pwd), verify=True)

  # print(myResponse.text)
# os.remove("shade-of-grey.jpeg") file busy
