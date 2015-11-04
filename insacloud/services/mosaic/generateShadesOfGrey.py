from PIL import Image
import requests
from requests.auth import HTTPDigestAuth
import json
import os

# TODO : variabilize and enhance (fix pb url for event :/)

url = 'http://localhost/api/pictures/'
data = {"event": 1, "hue" : 0}

for i in range(256):
  img = Image.new("L", (512, 512), i)
  img.save("shade-of-grey.jpeg","JPEG")
  files = {'image': ("shade-of-grey.jpeg", open("shade-of-grey.jpeg", 'rb'), 'image/jpg', {'Expires': '0'})}
  myResponse = requests.post(url, data=data, files=files, auth=("admin", "insacloud"), verify=True)

  print(myResponse.text)
# os.remove("shade-of-grey.jpeg") file busy
