#!/usr/bin/env python3
import os
import shutil
import psutil
import socket
import emails

#List sender and receiver 
sender="automation@example.com"
receiver= "<username>@example.com"
body="Please check your system and resolve the issue as soon as possible."

#path
path = "/"

#get disk usuage stats
#Report an error if available disk space is lower than 20%
stat = shutil.disk_usage(path)
statFreePercent = (stat.free/stat.total)*100
if statFreePercent < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

#get cpu usuage
#Report an error if CPU usage is over 80%
#calling psutil for 1 seconds
cpu_stat = psutil.cpu_percent(1)
if cpu_stat>80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

#get available RAM
#Report an error if available memory is less than 500MB
avail_RAM = psutil.virtual_memory()[4]
#convert 500 MB to bytes
memory_threshold = 500*1024*1024
if avail_RAM < memory_threshold:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
#Get local host ip address
hostip = socket.gethostbyname("localhost")
if hostip != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)
