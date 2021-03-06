from datetime import datetime, timedelta
import os
from twilio.rest import Client
import time
import requests
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqldatabase import UserInput
import os
from dotenv import load_dotenv
from contact_service import send_alert_mail

load_dotenv()
# create a Twilio client
account_sid = os.getenv("ACCOUNT_ID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# user phone number here
engine = create_engine('sqlite:///users_db.sqlite')
Session = sessionmaker(bind=engine)
sess= Session()
results = sess.query(UserInput).all()

while True:
    # send the SMS
    for item in results:   
        phone_number= item.userPhone
        city_name = item.city
        request_url = "https://api.waqi.info/feed/{}/?token=5938b35ceb20607ac17a113fe733908af8fbb1b7".format(city_name)
        req = requests.get(request_url)
        aqi_number = req.json()["data"]["aqi"]
        if aqi_number > 10:
            messaging_service_sid ="+19897350269"
            body = "Hello! The real-time Air Quality index at location {} is: {}".format(city_name, aqi_number)
            message = client.messages.create(
                from_=messaging_service_sid,
                to=phone_number,  
                body=body,
                schedule_type='fixed',
                send_at=datetime.utcnow(),
            )

            email = item.email
            print('email is ',email)
            send_alert_mail(email,body)
            print(message.sid)
            print("Sending messages.....")
        time.sleep(20)