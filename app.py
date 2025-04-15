from flask import Flask
from flask import request, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return('hello world')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)