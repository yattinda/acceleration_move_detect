from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_acceleration_data():
    json = request.get_json()
    First = json["first"]
    Second = json["second"]
    
    return "AAAAAAAAAAAAAAAAA"

if __name__ == '__main__':
    app.run()