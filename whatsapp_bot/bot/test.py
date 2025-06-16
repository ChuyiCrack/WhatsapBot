from SendWhatsapMessage import send_whatsapp_message

miNum = 526693280415
message = "Hello there"
send_whatsapp_message(miNum , message)

"""
{'object': 'whatsapp_business_account', 
'entry': [{'id': '719887507187879', 
'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15551577553', 'phone_number_id': '590771527464197'}, 
'contacts': [{'profile': {'name': 'Chuyi Xibille'}, 'wa_id': '5216693280415'}], 
'messages': [{'from': '5216693280415', 'id': 'wamid.HBgNNTIxNjY5MzI4MDQxNRUCABIYFjNFQjA0MEY5NTMxODg4ODA2RTQyNjkA', 'timestamp': '1749607711', 'text': {'body': 'gg'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
Mensaje de 5216693280415: gg
Response: 200 {"messaging_product":"whatsapp","contacts":[{"input":"5216693280415","wa_id":"5216693280415"}],"messages":[{"id":"wamid.HBgNNTIxNjY5MzI4MDQxNRUCABEYEjQwQUI4RUJCNDVFNUE0MURCRgA="}]}
[11/Jun/2025 02:08:33] "POST /webhook/ HTTP/1.1" 200 0
{
'object': 'whatsapp_business_account',
'entry': [{'id': '719887507187879',
'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15551577553',
 'phone_number_id': '590771527464197'},
 'statuses': [{'id': 'wamid.HBgNNTIxNjY5MzI4MDQxNRUCABEYEjQwQUI4RUJCNDVFNUE0MURCRgA=',
 'status': 'sent', 
 'timestamp': '1749607713', 'recipient_id': '5216693280415', 'conversation': {'id': '7297f76867bb041738b46977f9bf4c76', 'expiration_timestamp': '1749692160', 'origin': {'type': 'service'}}, 'pricing': {'billable': True, 'pricing_model': 'CBP', 'category': 'service'}}]}, 'field': 'messages'}]}]}


"""