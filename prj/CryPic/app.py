from flask import Flask, render_template
app = Flask(__name__)             # create an app instance


@app.route("/")                   # at the end point /
def index():                      # call method hello
    return render_template("index.html")         # which returns "hello world"


@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello " + name


if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app