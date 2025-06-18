import requests
from decouple import config


PROJECT_PHONE_NUMBER = config('PROJECT_PHONE_NUMBER')
ACCESS_TOKEN = config('ACCES_TOKEN')
URL = f"https://graph.facebook.com/v18.0/{PROJECT_PHONE_NUMBER}/messages"

def send_whatsapp_message(recipient_number, message_text):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "text",
        "text": {"body": message_text}
    }

    response = requests.post(URL, headers=headers, json=payload)
    print("Response:", response.status_code, response.text)


def send_whatsapp_menu(recipient_number):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": recipient_number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "header": {
        "type": "text",
        "text": "Menu Principal"
        },
        "body": {
        "text": "Escoge una opcion:"
        },
        "footer": {
        "text": "Hecho por Jesus Xibille"
        },
        "action": {
        "button": "Seleciona una opcion",
        "sections": [
            {
            "title": "Opciones",
            "rows": [
                {
                "id": "option1",
                "title": "Opcion 1",
                "description": ""
                },
                {
                "id": "option2",
                "title": "Opcion 2",
                "description": ""
                },
                {
                "id": "option3",
                "title": "Opcion 3",
                "description": ""
                }
            ]
            }
        ]
        }
    }
    }

    response = requests.post(URL, headers=headers, json=payload)
