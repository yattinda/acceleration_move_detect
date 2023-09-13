from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def test():
    return "Hello World"

@app.route('/', methods=["POST"])
def post_acceleration_data():
    json = request.get_json()
    First = json["first"]
    Second = json["second"]
    return "AAAAAAAAAAAAAAAAA"

if __name__ == '__main__':
    app.run()