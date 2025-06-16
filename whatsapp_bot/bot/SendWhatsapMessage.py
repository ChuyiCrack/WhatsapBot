import requests
from decouple import config


PROJECT_PHONE_NUMBER = config('PROJECT_PHONE_NUMBER')
ACCESS_TOKEN = config('ACCES_TOKEN')

def send_whatsapp_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/{PROJECT_PHONE_NUMBER}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "type": "text",
        "text": {"body": message_text}
    }

    response = requests.post(url, headers=headers, json=payload)
    print("Response:", response.status_code, response.text)
