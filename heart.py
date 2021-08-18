from flask import Flask, request
import pandas as pd
import numpy as np 
import pickle

app = Flask(__name__)
pickle_in = open('model_GB.pkl', 'rb')
model_GB = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_heart_attack():
    sex = request.args.get('sex')
    cp = request.args.get('cp')
    thalachh = request.args.get('thalachh') 
    exeng = request.args.get('exeng') 
    oldpeak = request.args.get('oldpeak')
    slp = request.args.get('slp')
    caa = request.args.get('caa')
    thall = request.args.get('thall') 

    prediction = model_GB.predict([[sex,cp,thalachh, exeng,oldpeak,slp,caa,thall]])

    return 'The predicted value is' + str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_heart_attack_file():
    df_test = pd.read_csv(request.files.get('file'))
    prediction = model_GB.predict(df_test)

    # sex = request.args.get('sex')
    # cp = request.args.get('cp')
    # thalachh = request.args.get('thalachh') 
    # exeng = request.args.get('exeng') 
    # oldpeak = request.args.get('oldpeak')
    # slp = request.args.get('slp')
    # caa = request.args.get('caa')
    # thall = request.args.get('thall') 

    # prediction = model_GB.predict([[sex,cp,thalachh, exeng,oldpeak,slp,caa,thall]])

    return 'The predicted values for the csv is: ' + str(list(prediction))





if __name__ == '__main__':
    app.run()

