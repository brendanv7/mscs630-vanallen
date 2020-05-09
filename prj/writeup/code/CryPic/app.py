from flask import Flask, render_template, request
from CryPic import CryPic
import time
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = os.getcwd() + "/uploads"

# Home page routes
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


# Route accessed on form submission from home page
@app.route('/generate', methods=['POST'])
def generate():
    # Get input data
    message = request.form['message']
    key = request.form['key']
    if not key:
        key = CryPic.generate_random_key()

    # Generate image
    crypic = CryPic(key)
    crypic.generate_pic(message)

    # pad is used to force browser to download the new image
    pad = time.time()
    return render_template("image.html", pad=pad, key=key)


# Route accessed from link on bottom of home page
@app.route("/decrypt")
def decrypt():
    return render_template("decrypt.html")


# Router accessed on form submission from decryption page
@app.route('/upload', methods=['POST'])
def upload():
    # Save the image
    image = request.files['image']
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

    # Get the key
    key = request.form['key']

    # Perform decryption
    crypic = CryPic(key)
    plaintext = crypic.decrypt_pic("uploads/" + image.filename)

    return render_template("view_message.html", message=plaintext)


if __name__ == "__main__":
    app.run(debug=True)
