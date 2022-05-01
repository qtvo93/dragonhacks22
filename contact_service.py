import requests
import os
from dotenv import load_dotenv

def send_alert_mail(email,message):
    requests.post(
        "https://api.mailgun.net/v3/sandboxc0031d380d124aa09cff1652f0bc6e8a.mailgun.org/messages",
        auth=("api", "43bfcd764d3f5e4ac9ac763438fdb98d-53ce4923-62fc4b58"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxc0031d380d124aa09cff1652f0bc6e8a.mailgun.org>",
            "to": email,
            "subject": "Air Quality index",
            "text": message})

