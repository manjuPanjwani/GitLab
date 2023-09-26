#!/usr/bin/env python3
import json
import sys
import os
from datetime import date
import reports 
import emails 

dir="./supplier-data/descriptions/"
reportFile = "/tmp/ processed.pdf"

def readLines(supp_data_desc):
  #read lines
  with open(dir+supp_data_desc, mode='r',encoding='UTF-8') as fb_file:
    lines = fb_file.read().splitlines()
  return lines

def readSupplierData():
  dir_list = os.listdir(dir)
  names=[]
  weights=[]
  for file in dir_list:
    with open(dir+file) as f:
      for ln in f:
        line = ln.strip()
        if len(line)<=10 and len(line)>0 and "lb" not in line:
          fr_name="name: " + line
          names.append(fr_name)
        if "lbs" in line:
          fr_weight="weight: "+ line
          weights.append(fr_weight)

  """Turns the data into fruit summary"""
    summary=""
    for name,weight in zip(names,weights):
        summary+= name +'</br>' + weight +'</br>' +'</br>'
    return summary     

    

def generate_summary():
    """Process the JSON data and generate a full report out of it."""
    summary = readSupplierData()
    dt = datetime.date.today().strftime("%B  %d, %Y")
    title = "Processed Update on " + dt
     
    # TODO: turn this into a PDF report
    #attachment, title, body text
    reports.generate_report(title, summary,reportFile)


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    generate_summary()
    
    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "USERNAME@example.com"
    subject="Upload completed - Online Fruit Store"
    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    msg = emails.generate_email(sender, receiver,subject, body,reportFile)
    emails.send_email(msg)

if __name__ == "__main__":
    main(sys.argv)
