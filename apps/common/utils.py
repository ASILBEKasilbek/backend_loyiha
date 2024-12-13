import random
from twilio.rest import Client

def generate_verification_code():
    return str(random.randint(100000, 999999))  # 6 xonali kod

def send_sms(phone_number, code):
    # Twilio hisob ma'lumotlarini kiriting
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your verification code is: {code}",
        from_=twilio_phone_number,
        to=phone_number
    )
    return message.sid
