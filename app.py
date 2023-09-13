from flask import Flask, request
from flask_cors import CORS
import json
import pandas as pd
from math import sqrt

app = Flask(__name__)
CORS(app)

Mets = {
    "stand" : 2,
    "walk"  : 4,
    "jump"  : 6,
}

jump_min = 5
walk_min = 2

def culc_acceleration(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def culc_cal(acceleration, second, weight):
    if acceleration > jump_min:
        mets = "jump"
    elif walk_min > acceleration:
        mets = "stand"
    else:
        mets = "walk"
    return float(Mets[mets] * (second / 3600) * weight * 1.05)

@app.route('/', methods=["GET"])
def test():
    return "Hello World"

@app.route('/', methods=["POST"])
def post_acceleration_data():
    total_cal = 0.0
    first_index = 0
    last_index = 10
    df_acceration = pd.DataFrame(columns=["acceration"])
    posted_json = request.get_json()
    weight = posted_json["weight"]
    raw_df_acceration = posted_json['DATA']
    for i in range(len(raw_df_acceration)):
        acceration = culc_acceleration(raw_df_acceration[i]["x"], raw_df_acceration[i]["y"], raw_df_acceration[i]["z"])
        df_acceration.loc[i] = acceration
    while last_index < len(raw_df_acceration):
        target = df_acceration[first_index:last_index]
        acceration_max = float(target.max(axis = 0))
        total_cal += culc_cal(acceration_max, 1, weight)
        first_index += 10
        last_index += 10
    return str(total_cal)

if __name__ == '__main__':
    app.run()