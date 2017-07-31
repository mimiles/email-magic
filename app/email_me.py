import os
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

# AUTHENTICATE

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS

subject = "Email Magic from the SendGrid Python Library!"
my_email = Email("mm8932@stern.nyu.edu")
from_email = my_email
to_email = my_email
content = Content("text/plain", "Email magic, brought to you by Python!")
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code)
print(response.body)
print(response.headers)
