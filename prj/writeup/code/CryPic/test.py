from CryPic import CryPic
from PIL import Image
import time

mykey = "dude"
gen = CryPic(mykey)
mymsg = "this is a message"

# Create image
gen.generate_pic(mymsg)

# Decrypt image
gen2 = CryPic(mykey)
# image = Image.open("uploads/new1.png")
pt = gen2.decrypt_pic('static/images/new1.png')

# print(ct)
print(pt)

# # Encrypt
# ct = gen.generate_pic(mymsg)
#
# # Create pixels
# ctArr = gen.generate_pixels(ct)
#
# # Extract ciphertext
# ctBy = gen.extract_ciphertext(ctArr)
#
# # Decrypt
# pt = gen.decrypt_pic(ctBy)
#
# print(ct)
# print(len(ctArr))
# print(len(ctBy))
# print(pt)
