#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
    #Basic email format
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["subject"] = subject
    message.set_content(body)

    #Process attachment to add to email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/',1)

    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap, read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    return message

def send(message):

    #Sends message to the configured SMTP
    mail.server = smtplib.SMTP('localhost')
    mail.server.send_message(message)
    mail.server.quit()
