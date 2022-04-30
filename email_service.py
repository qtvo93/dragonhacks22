from datetime import datetime, timedelta
import os
from twilio.rest import Client
import time
import requests
# create a Twilio client
account_sid = "AC2e3aef6ecd5206ee492f831333615388"
auth_token = "b627fbe4ad19b6aad50e2a8fb3f8fe0d"
client = Client(account_sid, auth_token)

# user phone number here
phone_number = '+12672664793'

# schedule message to be sent 1 minutes after current time
city_name = "philadelphia"
while True:
    # send the SMS
    request_url = "https://api.waqi.info/feed/{}/?token=5938b35ceb20607ac17a113fe733908af8fbb1b7".format(city_name)
    req = requests.get(request_url)
    aqi_number = req.json()["data"]["aqi"]
    messaging_service_sid ="+19897350269"
    message = client.messages.create(
        from_=messaging_service_sid,
        to=phone_number,  # ← your phone number here
        body="Hello user! The real-time Air Quality index at location ??? is: {}".format(aqi_number),
        schedule_type='fixed',
        send_at=datetime.utcnow(),
    )

    print(message.sid)
    print("Sending messages.....")
    time.sleep(60*30)