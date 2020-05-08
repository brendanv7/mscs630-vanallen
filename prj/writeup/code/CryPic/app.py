from flask import Flask, render_template, request, redirect
from CryPic import CryPic
import time
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = os.getcwd() + "/uploads"


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():
    # Get input data
    message = request.form['message']
    key = request.form['key']

    # Pad the message if less than 16 characters
    while len(message) < 16:
        message += " "

    # Generate image
    crypic = CryPic(key)
    crypic.generate_pic(message)
    # print("Message: " + message + " Key: " + key)

    pad = time.time()
    return render_template("image.html", pad=pad)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    image = request.files['image']
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

    key = request.form['key']
    crypic = CryPic(key)
    plaintext = crypic.decrypt_pic("uploads/" + image.filename)
    print(plaintext)

    return render_template("decrypt.html", message=plaintext)


@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello " + name


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app
