import requests
import os
from dotenv import load_dotenv

def send_alert_mail(email,message):
    requests.post(
        "https://api.mailgun.net/v3/sandboxc0031d380d124aa09cff1652f0bc6e8a.mailgun.org/messages",
        auth=("api", "a4c38c48c3e3071f53ca7ae5bb957ae0-53ce4923-878def16"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxc0031d380d124aa09cff1652f0bc6e8a.mailgun.org>",
            "to": email,
            "subject": "Air Quality index",
            "text": message})

