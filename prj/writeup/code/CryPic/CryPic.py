from AESCipher import AESCipher
from random import randint
from PIL import Image
import numpy


class CryPic:
    def __init__(self, key):
        self.aes = AESCipher(key)

    # Creates an image from the encrypted message
    def generate_pic(self, message):
        # Encrypt the message
        ciphertext = self.aes.encrypt(self.clean_message(message))

        # Generate pixels for the image
        pixels = self.generate_pixels(ciphertext)
        array = numpy.array(pixels, dtype=numpy.uint8)

        # Use PIL to create an image from the array of pixels
        new_image = Image.fromarray(array)
        new_image.save('static/images/new1.png')

        # Return value is for testing purposes only
        return ciphertext

    # Extracts the ciphertext from the image and decrypts it
    def decrypt_pic(self, image_path):
        image = Image.open(image_path)
        ciphertext = self.extract_ciphertext(image)
        try:
            plaintext = self.aes.decrypt(ciphertext)
        except ValueError:
            print("Invalid image")
            plaintext = ""

        return plaintext

    # Generates a 2d array of pixel values from the given ciphertext
    @staticmethod
    def generate_pixels(ciphertext):
        cipher_str = ciphertext.decode()
        pixels = []
        pixel_row = []
        col = 0
        for char in cipher_str:
            # Red and green values are always random
            red = randint(0, 255)
            green = randint(0, 255)

            # Blue value holds the ciphertext character
            blue = ord(char)

            pixel_row.append([red, green, blue])
            col += 1
            if col == 8:
                pixels.append(pixel_row)
                pixel_row = []
                col = 0

        return pixels

    # Extracts the ciphertext string from the image
    @staticmethod
    def extract_ciphertext(image):
        pixels = list(image.getdata())
        ciphertext = []
        for pixel in pixels:
            # Blue value holds the ciphertext character - index 2
            ciphertext.append(chr(pixel[2]))

        ciphertext = ''.join(ciphertext)
        return ciphertext

    # Generates a random string (len = 16) to be used as a key
    @staticmethod
    def generate_random_key():
        key = ""
        for i in range(16):
            key += chr(randint(32, 126))

        return key

    # Pads the message if necessary to avoid value errors in crypto module
    @staticmethod
    def clean_message(message):
        while len(message) < 16:
            message += " "
        while len(message) in range(48, 64):
            message += " "
        while len(message) in range(96, 112):
            message += " "
        while len(message) in range(144, 160):
            message += " "
        while len(message) in range(192, 208):
            message += " "
        while len(message) in range(240, 256):
            message += " "

        return message
