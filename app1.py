# -*- coding: utf-8 -*-
"""
Event:IBM Hack challenge 2020
@team members: Barathkumar G  id:191cs138
               Ajay S         id:191cs110
               Dhanush s      id:191cs156
Guide name: Ms Malathi T AP/CSE
Mentor name : Mr Hemant Kumar Gahlot   AI Developer/IBM
              Ms Gayatri   AI Developer/IBM
"""

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    ws=int(request.form['windspeed'])
    di=request.form['wind direction']
    if di=="east" or "EAST" or "East":
        di=1
    elif di=="west" or "WEST" or "West":
        di=2
    elif di=="north" or "North" or "NORTH":
        di=3
    elif di=="south" or "South" or "SOUTH":
        di=4
    elif di=="northeast" or "Northeast" or "NORTHEAST":
        di=5
    elif di=="northwest"or "Northwest" or "NORTHWEST":
        di=6
    elif di=="southeast" or "SOUTHEAST" or "Southeast":
        di=7
    elif di=="southwest" or "SOUTHWEST" or "Southwest":
        di=8
    int_features=[]
    int_features.append(ws)
    int_features.append(di)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = abs(np.around(prediction[0][0],2))
    if float(output)>2.25:
        result="The Output power Satisfy the Company's need"
    else:
         result="The Output Power Unable to Satisfy the Company's need"
    return render_template('index.html', prediction_text='The power to be generated is {} Mega Watts'.format(output),a=result)


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)