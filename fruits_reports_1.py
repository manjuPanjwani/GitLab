#!/usr/bin/env python3
import json
import sys
from datetime import date
from reports import generate as report
from emails  import generate as email_generate
from emails  import send as email_send

dir="supplier-data/descriptions/"

def readLines(supp_data_desc):
  #read lines
  with open(dir+supp_data_desc, mode='r',encoding='UTF-8') as fb_file:
    lines = fb_file.read().splitlines()
  return lines

def readSupplierData():
  dir_list = os.listdir(dir)
  fruitsDescription=[]
  keys=["name","weight","description"]
  for file in dir_list:
      lines = readLines(file)
      fruitsDescription.append(dict(zip(keys,lines)))
  return fruitsDescription

def fruits_dict_to_table(fruit_data):
    """Turns the data in car_data into a list of lists."""
    table_data = ["name", "weight"]
    for item in fruit_data:
        table_data.append([item["name"],item["weight"]])
    return table_data

def generate_report():

    """Process the JSON data and generate a full report out of it."""
    fruitDescription = readSupplierData()
    table_data = fruits_dict_to_table(fruitDescription)
    today=date.today()
    
    # TODO: turn this into a PDF report
    report('/tmp/ processed.pdf', "Processed Update on " + today, table_data,newLineChars=1)
    
def main(argv):
    """Process the JSON data and generate a full report out of it."""
    generate_report()
    
    #data = load_data("/home/USERNAME/car_sales.json")
    #summary = process_data(data)
    #new_summary = ''.join(summary)
    #print(summary)
    # TODO: turn this into a PDF report
    #report('/tmp/cars.pdf', "Cars report", new_summary, cars_dict_to_table(data))
    # TODO: send the PDF report as an email attachment
    #msg = email_generate("automation@example.com", "USERNAME@example.com",
         #                "Sales summary for last month", new_summary, "/tmp/cars.pdf")
    #email_send(msg)

if __name__ == "__main__":
    main(sys.argv)
