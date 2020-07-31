
from flask import Flask , jsonify , request


app = Flask(__name__)
@app.route("/")

def dummy_api():
    input_recieved=request.get_json()

    return jsonify({"input was" : input_recieved})

if __name__ == "__main__":
    app.run()
