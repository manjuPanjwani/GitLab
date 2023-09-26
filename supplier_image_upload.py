#!/usr/bin/env python3

import os
import requests

url = 'http://34.118.240.130/upload/'
dir = './supplier-data/images/'

#dir_list=os.listdir(dir)
for img_file in os.listdir('./supplier-data/images'):
    if img_file.endswith(".jpeg"):
        with open(dir+img_file,'rb') as opened:
            r = requests.post(url,files={'file':opened})
