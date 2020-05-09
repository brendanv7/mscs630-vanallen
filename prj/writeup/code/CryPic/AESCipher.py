import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random


class AESCipher:
    BLOCK_SIZE = 16

    def __init__(self, key):
        self.key = key

    # Encrypts the given message into a byte stream
    def encrypt(self, raw):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    # Decrypts the given byte stream into the original message
    def decrypt(self, enc):
        key = hashlib.sha256(self.key.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return bytes.decode(self.unpad(cipher.decrypt(enc[16:])))

    # Pads the input to match the AES block size
    def pad(self, s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * \
               chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)

    # Unpads the input to retrieve the original
    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]
