from django.urls import path
from .views import webhook

urlpatterns = [
    path('', webhook, name='whatsapp_webhook'),
]