import hashlib
import os.path
import pickle
import base64
from googleapiclient.discovery import build
from flask import render_template, session
from email.mime.text import MIMEText

token_file = os.path.dirname(__file__) + "/../auth/token.pickle"

if os.path.exists(token_file):
    with open(token_file, 'rb') as token:
        creds = pickle.load(token)

if 'creds' in locals():
    service = build('gmail', 'v1', credentials=creds)
else:
    print("warning: credict file not found")

def send_email(to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = "me"
  message['subject'] = subject
  message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")}

  message = (service.users().messages().send(userId="me", body=message).execute())
  return message

def password_hash(string):
    return hashlib.sha256(bytes(string+'lin', encoding = "utf8")).hexdigest()

def my_render_template(*arg, **karg):
    name=None
    id=None
    userType=None
    if 'username' in session:
        name=session['username']
    if 'id' in session:
        id=session['id']
    if 'type' in session:
        userType=session['type']
    return render_template(*arg, **karg, name=name, id=id, usertype=userType)

