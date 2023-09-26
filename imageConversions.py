#!/usr/bin/env python3

from PIL import Image
import os

directory = "images/"
out_directory = "/opt/icons/"

def convertImageFile():
   #read files from the folder
   for fname in os.listdir(directory):
      if fname != ".DS_Store":
         img = Image.open(os.path.join(directory,fname))
         img = img.rotate(-90)
         img = img.resize((128,128))
         img = img.convert("RGB")
         img.save(os.path.join(out_directory,fname+".jpeg"))

if __name__ == "__main__":
  convertImageFile()
  sys.exit(0)
