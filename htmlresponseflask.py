
from flask import Flask


app = Flask(__name__)
@app.route("/")

def dummy_api():
    return "Hello kpriya"

if __name__ == "__main__":
    app.run()
