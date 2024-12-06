from rest_framework.views import APIView
from rest_framework.response import Response
from utils.encryption import decrypt_message

class ReceiveMessageAPIView(APIView):
    def post(self, request):
        encrypted_message = request.body.decode()  # Get the encrypted message from the request
        decrypted_message = decrypt_message(encrypted_message)  # Decrypt the message

        return Response({"status": "Message received", "message": decrypted_message})
