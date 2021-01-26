
#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
ogpath = "/home/student-04-aa1c9ff63256/supplier-data/images/"
upload_list = []

#iterate through the dir and post each .jpeg to the url
for images in os.listdir(ogpath):
  try:
    if images.endswith(".jpeg"):
      with open("{folder}{name}".format(folder=ogpath, name=images), "rb") as opened:
        r = requests.post(url, files={'file': opened})
        print(r.status_code)
        print(r.text)
  except:
    print("Failed try")
