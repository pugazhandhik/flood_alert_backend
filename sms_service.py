from twilio.rest import Client
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER
)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(numbers, message):
    for number in numbers:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=number
        )
