from django.utils.deprecation import MiddlewareMixin
from utils.encryption import encrypt_message, decrypt_message

class EncryptionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """Decrypt incoming request data"""
        if request.body:
            request._body = decrypt_message(request.body.decode())

    def process_response(self, request, response):
        """Encrypt outgoing response data"""
        if response.content:
            response.content = encrypt_message(response.content.decode())
        return response
