from AESCipher import AESCipher
from random import randint
from PIL import Image
import numpy
import copy


class CryPic:
    def __init__(self, key):
        self.aes = AESCipher(key)

    def generate_pic(self, message):
        ciphertext = self.aes.encrypt(message)

        pixels = self.generate_pixels(ciphertext)
        array = numpy.array(pixels, dtype=numpy.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save('static/images/new1.png')

        return ciphertext

    def decrypt_pic(self, image_path):
        image = Image.open(image_path)
        ciphertext = self.extract_ciphertext(image)
        plaintext = self.aes.decrypt(ciphertext)
        return plaintext

    # Generates a 2d array of pixel values from the given ciphertext
    def generate_pixels(self, ciphertext):
        cipher_str = ciphertext.decode()
        pixels = []
        pixel_row = []
        col = 0
        for char in cipher_str:
            red = randint(0, 255)
            green = randint(0, 255)
            blue = ord(char)
            pixel_row.append([red, green, blue])
            col += 1
            if col == 8:
                pixels.append(pixel_row)
                pixel_row = []
                col = 0

        return pixels

    def extract_pixels(self, image):
        return list(image.getdata())

    def extract_ciphertext(self, image):
        pixels = list(image.getdata())
        ciphertext = []
        # for pixel_row in pixels:
        #     for pixel in pixel_row:
        #         ciphertext.append(chr(pixel[2]))
        for pixel in pixels:
            ciphertext.append(chr(pixel[2]))

        ciphertext = ''.join(ciphertext)
        return ciphertext
