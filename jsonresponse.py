# This file shows how to get json formatted output from postapi

from flask import Flask , jsonify


app = Flask(__name__)
@app.route("/")

def dummy_api():
    return jsonify(data = "Hello kpriya")

if __name__ == "__main__":
    app.run()
