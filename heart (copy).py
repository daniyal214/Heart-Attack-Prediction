from flask import Flask, request
import pandas as pd
import numpy as np 
import pickle
import flasgger
from flasgger import Swagger



app = Flask(__name__)
Swagger(app)


pickle_in = open('model_GB.pkl', 'rb')
model_GB = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict', methods=['GET'])
def predict_heart_attack():

    """ Let's predict the Heart Attack
    ---
    parameters:
        - name: sex
          in: query
          type: number
          required: true
        - name: cp
          in: query
          type: number
          required: true
        - name: thalachh
          in: query
          type: number
          required: true
        - name: exeng
          in: query
          type: number
          required: true
        - name: oldpeak
          in: query
          type: number
          required: true
        - name: slp
          in: query
          type: number
          required: true
        - name: caa
          in: query
          type: number
          required: true
        - name: thall
          in: query
          type: number
          required: true   
    responses:
          200:
            description: The output values       
    """

    sex = request.args.get('sex')
    cp = request.args.get('cp')
    thalachh = request.args.get('thalachh') 
    exeng = request.args.get('exeng') 
    oldpeak = request.args.get('oldpeak')
    slp = request.args.get('slp')
    caa = request.args.get('caa')
    thall = request.args.get('thall') 

    prediction = model_GB.predict([[sex,cp,thalachh, exeng,oldpeak,slp,caa,thall]])

    if prediction == 1:
        res = 'You are prone to Heart Attack'
    else:
        res = 'You are not prone to Heart Attack'

    return res

@app.route('/predict_file', methods=['POST'])
def predict_heart_attack_file():

    """Let's predict Heart Attack
    ---

    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
          200:
            description: The output values
    """

    df_test = pd.read_csv(request.files.get('file'))
    prediction = model_GB.predict(df_test)

    return 'The predicted values for the csv is: ' + str(list(prediction))





if __name__ == '__main__':
    app.run()

