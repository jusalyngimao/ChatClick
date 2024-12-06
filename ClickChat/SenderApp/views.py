from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class SendMessageAPIView(APIView):
    def post(self, request):
        message = request.data.get('message')
        # Encrypt the message before sending it
        encrypted_message = encrypt_message(message)

        # Send the encrypted message to ReceiverApp
        response = requests.post('http://receiverapp-url/receive/', data=encrypted_message)
        
        return Response({"status": "Message sent", "response": response.text})
