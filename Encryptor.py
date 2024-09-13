from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


class Encryptor:
    def __init__(self):
        self.block_size = AES.block_size

    def encrypt(self, text_to_encrypt, secret_key):
        # pad the secret key to ensure it's 16, 24, or 32 bytes long
        secret_key = self._pad_key(secret_key)

        # Generate a random Initialization vector
        iv = get_random_bytes(self.block_size)

        # Create cipher object and encrypt
        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(text_to_encrypt.encode(), self.block_size))

        # Combine IV and encrypted data
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt(self, text_to_decrypt, secret_key):
        # Ensure the key is 16, 24, or 32 bytes long
        secret_key = self._pad_key(secret_key)

        # Decode the base64 encoded string
        enc = base64.b64decode(text_to_decrypt.encode('utf-8'))

        # Extract IV and encrypted data
        iv = enc[:self.block_size]
        encrypted_data = enc[self.block_size:]

        # Create cipher object and decrypt
        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), self.block_size)

        return decrypted_data.decode('utf-8')

    def _pad_key(self, key):
        # Ensure the key is 16, 24, or 32 bytes long
        if len(key) <= 16:
            return key.ljust(16, b'\0')
        elif len(key) <= 24:
            return key.ljust(24, b'\0')
        else:
            return key[:32].ljust(32, b'\0')
