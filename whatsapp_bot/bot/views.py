import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from .SendWhatsapMessage import send_whatsapp_message

VERIFY_TOKEN = config('VERIFY_TOKEN')

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('Verification token mismatch', status=403)

    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            # Extrae informacion del json obtenido
            entry = data['entry'][0]
            sender_name = entry['changes'][0]['value']['contacts'][0]['profile']['name']
            print(data)
            message_data = entry['changes'][0]['value']['messages'][0]
            sender_telephone = message_data['from']  #Telefono del Usuario
            message_text = message_data['text']['body']  # Mensaje obtenido

            print(f"Mensaje de {sender_telephone}: {message_text}")

            message_to_send = f"""
                Hola, Gracias por comunicarte {sender_name} y dar tu opinion {message_text}.
            """
            #Regresar el mensaje
            #send_whatsapp_message(sender_telephone, message_to_send)

        except KeyError as e:
            return HttpResponse(status=202)

        except Exception as e:
            print("No se pudo completar el mandado del mensaje", str(e))
            return HttpResponse('Hubo algun eror', status=406)

        return HttpResponse(status=200)

    return HttpResponse('Method not allowed', status=405)
