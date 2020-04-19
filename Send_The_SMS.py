from twilio.rest import Client #TwilioRestClient has been removed from the library
from Credentials import account_sid, auth_token, cell, twilio 

client = Client(account_sid, auth_token) 

MainMsg = "The main message you want to send"

message = client.messages.create(to=cell, from_=twilio, body=MainMsg)


