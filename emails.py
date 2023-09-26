#!/usr/bin/env python3
import mimetypes
import os
import smtplib
import email.message


#sender, receiver, subject, body, attachement
def generate_email(sender, receiver,subject,body,fileName):
    msg=email.message.EmailMessage()
    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject
    msg.set_content(body)

    attachment_path=os.path.basename(fileName)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
        msg.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))
    return msg

def send_email(msg):
    mail_server=smtplib.SMTP('localhost')
    mail_server.send_message(msg)
    mail_server.quit()

def generate_error_email(sender, receiver, subject, body):
    msg=email.message.EmailMessage()
    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject
    msg.set_content(body)

    return msg
    
