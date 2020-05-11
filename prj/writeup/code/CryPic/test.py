from CryPic import CryPic

key = "blank message"
message = "hey"

crypic = CryPic(key)

# Create image
ct = crypic.generate_pic(message)

# Decrypt image
crypic = CryPic(key)

pt = crypic.decrypt_pic('static/images/new1.png')

print("Message:                  " + message)
print("Key:                      " + key)
print("Message after decryption: " + pt)
print(len(ct))
