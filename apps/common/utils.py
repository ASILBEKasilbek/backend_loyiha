import random
# from twilio.rest import Client

def generate_verification_code():
    return str(random.randint(100000, 999999))  # 6 xonali kod

def send_sms(phone_number, code):
    account_sid = ''
    auth_token = ''
    twilio_phone_number = '+1 361 282 9798'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your verification code is: {code}",
        from_=twilio_phone_number,
        to=phone_number
    )
    return message.sid
