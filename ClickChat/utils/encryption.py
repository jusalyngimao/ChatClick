from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

# Get the encryption key from the environment variable
SECRET_KEY = os.getenv('ENCRYPTION_KEY', 'default-secret-key')  # Default fallback key

def encrypt_message(message):
    """Encrypt a message using AES encryption"""
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

def decrypt_message(encrypted_message):
    """Decrypt a message using AES decryption"""
    raw = base64.b64decode(encrypted_message)
    iv = raw[:16]
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(raw[16:]), AES.block_size).decode()
