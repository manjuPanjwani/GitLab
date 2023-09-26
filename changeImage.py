
#!/usr/bin/env python3
      
from PIL import Image
import os
         
directory = "~/supplier-data/images/"
out_directory = "~/supplier-data/images/"

def convertImageFile():   
   #read files from the folder
   for fname in os.listdir(directory):
      if fname.endswith(".tiff"):
         split_fname=fname.split(".")
         name=split_fname[0]+".jpeg"
         img = Image.open(directory+fname).convert("RGB"))
         #img = img.rotate(-90)
         img.resize((600,400)).save(directory+name,"JPEG")

    
if __name__ == "__main__":
  convertImageFile()
