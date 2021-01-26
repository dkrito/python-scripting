#!/usr/bin/env python3

import os
from PIL import Image

#starting path to images
image_path = "/home/student-04-aa1c9ff63256/supplier-data/images/"

#scan directory in path and iterate through files
for entry in os.scandir(image_path):
  try:
    im = Image.open(image_path + entry.name)
    convertedimage = im.rotate(270).resize((600,400)).convert("RGB")
    convertedimage.save(image_path + os.path.splitext(entry.name)[0] + ".jpeg", "JPEG")
  except:
    print("Not a tiff")