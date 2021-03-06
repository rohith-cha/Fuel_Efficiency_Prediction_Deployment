# FLask API is a tool which helps to connect webs servers to your project

from flask import Flask, render_template,url_for,request,jsonify
import os
import pickle
import pandas as pd
import joblib
import numpy as np
import sklearn
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/result',methods=['POST','GET'])
def result():
    cylinders=int(request.form["cylinders"])
    displacement=int(request.form["displacement"])
    horsepower=int(request.form["horsepower"])
    weight=int(request.form["weight"])
    acceleration=int(request.form["acceleration"])
    model_year=int(request.form["model_year"])
    origin=int(request.form["origin"])
    
    values=[[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]]
    
    sc = None
    with open('scaler.pkl', 'rb') as f:
     sc = pickle.load(f)
        
    values =sc.transform(values)

    model =load_model("model.h5")
    
    prediction=model.predict(values)
    prediction=float(prediction)
    
    return render_template('home.html',prediction_text="You car fuel efficiency is {}".format( prediction))
    
if __name__=="__main__":
    app.run(debug=True)
