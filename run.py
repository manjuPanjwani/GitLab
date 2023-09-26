#!/usr/bin/env python3
import json
import os
import requests

#Generate the JSON objects from the supplier data
dir="./supplier-data/descriptions/"
img_dir="./supplier-data/images/
url = 'http://localhost/fruits/'

def readLines(supp_data_desc):
  #read lines
  with open(dir+supp_data_desc, mode='r',encoding='UTF-8') as fb_file:
    lines = fb_file.read().splitlines()
  return lines
          
def post_request(fruits):
  response = requests.post(url, json=fruits)
  if response.ok:
    print("ADDED")
  else:
    print("ERROR"+response.status_code)

def readSupplierData():
  dir_list = os.listdir(dir)
  fruits={}
  keys=["name","weight","description","image_name"]
  
  for file in dir_list:
    i=0
    with open(dir+file) as fl:
      for line in fl:
         ln = line.strip()
         if "lbs" in ln:
           nline=ln.split()
           wght=int(nline[0])
           fruits["weight"]=wght
           i+=1
          else:
            try:
              fruits[keys[i]]=ln
              i+=1
            except:
              fruits[keys[2]=ln
      split_f=file.split(".")
      name=split_f[0]+".jpeg"
      for fle in os.listdir(img_dir):
        if fle==name:
           fruits["image_name"]=name
      post_request(fruits)
      fruits.clear()
  
    
if __name__ == "__main__":
  readSupplierData()
